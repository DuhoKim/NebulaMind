import json
import time
import asyncio
import logging
import httpx
import redis
import platform
import socket
import weakref
from urllib.parse import urlparse
from typing import Any, Optional, Dict
from app.config import settings, BATCH_SAFE_DEFAULT_MODEL
from app.services.llm_utils import clean_llm_response

logger = logging.getLogger(__name__)

class ModelFootprints:
    # Local Host Names: studio (Mac Studio port 11434) and pro (Mac Pro port 11435 over tunnel)
    HOSTS = {
        "studio": "http://localhost:11434/v1",
        "pro": "http://localhost:11435/v1",
    }

    # Model Footprints Map
    FOOTPRINTS = {
        "llama3.3:70b": {
            "host": "studio",
            "tier": "heavy",
            "vram_gb": 42,
            "slots": 1,
            "cold_load": 30
        },
        "gpt-oss:120b": {
            "host": "studio",
            "tier": "heavy",
            "vram_gb": 65,
            "slots": 1,
            "cold_load": 45
        },
        "astrosage-70b:latest": {
            "host": "studio",
            "tier": "heavy",
            "vram_gb": 42,
            "slots": 1,
            "cold_load": 30
        },
        "astrosage-70b": {
            "host": "studio",
            "tier": "heavy",
            "vram_gb": 42,
            "slots": 1,
            "cold_load": 30
        },
        "qwen3.6:35b-a3b-nvfp4": {
            "host": "studio",
            "tier": "medium",
            "vram_gb": 23,
            "slots": 1,
            "cold_load": 15
        },
        "qwen3.6:27b-nvfp4": {
            "host": "studio",
            "tier": "medium",
            "vram_gb": 17,
            "slots": 1,
            "cold_load": 15
        },
        "gpt-oss:20b": {
            "host": "studio",
            "tier": "light",
            "vram_gb": 13,
            "slots": 0,
            "cold_load": 10
        },
        "vanta-research/atom-astronomy-7b:latest": {
            "host": "studio",
            "tier": "light",
            "vram_gb": 5,
            "slots": 0,
            "cold_load": 5
        },
        "vanta-research/atom-astronomy-7b": {
            "host": "studio",
            "tier": "light",
            "vram_gb": 5,
            "slots": 0,
            "cold_load": 5
        },
        "atom-astronomy-7b": {
            "host": "studio",
            "tier": "light",
            "vram_gb": 5,
            "slots": 0,
            "cold_load": 5
        }
    }

    @classmethod
    def get_info(cls, model_name: str) -> Optional[Dict[str, Any]]:
        if not model_name:
            return None
        # Exact match
        if model_name in cls.FOOTPRINTS:
            return cls.FOOTPRINTS[model_name]
        # Substring/prefix match
        for key, value in cls.FOOTPRINTS.items():
            if model_name.startswith(key) or key.startswith(model_name):
                return value
        return None


_OLLAMA_LIVENESS_CACHE: dict[str, tuple[float, bool]] = {}
_PERSISTENT_CLIENTS: "weakref.WeakKeyDictionary[asyncio.AbstractEventLoop, httpx.AsyncClient]" = weakref.WeakKeyDictionary()
PREFLIGHT_TIMEOUT_SECONDS = 1.0
FALLBACK_TIMEOUT_SECONDS = 90


def _is_local_url(base_url: str) -> bool:
    host = urlparse(base_url).hostname or ""
    return host in {"localhost", "127.0.0.1", "::1"}


def _http_timeout(seconds: float) -> httpx.Timeout:
    seconds = max(1.0, float(seconds))
    return httpx.Timeout(
        timeout=seconds,
        connect=min(5.0, seconds),
        read=seconds,
        write=min(10.0, seconds),
        pool=min(5.0, seconds),
    )

def get_persistent_client() -> httpx.AsyncClient:
    loop = asyncio.get_running_loop()
    client = _PERSISTENT_CLIENTS.get(loop)
    if client is not None and not client.is_closed:
        return client

    socket_options = [
        (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
    ]
    if platform.system() == "Darwin":
        # macOS: TCP_KEEPALIVE is 0x10
        socket_options.append((socket.IPPROTO_TCP, 0x10, 30))
    else:
        if hasattr(socket, "TCP_KEEPIDLE"):
            socket_options.append((socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 30))
        if hasattr(socket, "TCP_KEEPINTVL"):
            socket_options.append((socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10))
        if hasattr(socket, "TCP_KEEPCNT"):
            socket_options.append((socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5))

    limits = httpx.Limits(
        max_connections=20,
        max_keepalive_connections=5,
        keepalive_expiry=60.0,
    )
    transport = httpx.AsyncHTTPTransport(
        socket_options=socket_options,
        limits=limits,
    )
    client = httpx.AsyncClient(transport=transport)
    _PERSISTENT_CLIENTS[loop] = client
    return client


class InferenceScheduler:
    def __init__(self, redis_client=None):
        self._redis = redis_client

    def _get_redis(self):
        if self._redis:
            return self._redis
        try:
            return redis.from_url(
                settings.REDIS_URL,
                decode_responses=True,
                socket_timeout=5.0,
                socket_connect_timeout=3.0,
            )
        except Exception as e:
            logger.warning(f"[InferenceScheduler] Redis connection failed: {e}")
            return None

    async def _ollama_alive(self, base_url: str) -> bool:
        now = time.time()
        cached = _OLLAMA_LIVENESS_CACHE.get(base_url)
        if cached and now - cached[0] < 10.0:
            return cached[1]
        
        probe_url = base_url.rstrip("/").removesuffix("/v1") + "/api/tags"
        try:
            client = get_persistent_client()
            r = await client.get(probe_url, timeout=0.5)
            alive = r.status_code == 200
        except Exception:
            alive = False
            
        _OLLAMA_LIVENESS_CACHE[base_url] = (now, alive)
        return alive

    async def _is_circuit_breaker_active(self) -> bool:
        r = self._get_redis()
        if not r:
            return False
        try:
            blackout = await asyncio.to_thread(r.get, "ollama:circuit_breaker:blackout")
            return bool(blackout)
        except Exception as e:
            logger.warning(f"[InferenceScheduler] Error checking circuit breaker: {e}")
            return False

    async def _record_failure(self):
        r = self._get_redis()
        if not r:
            return
        try:
            now = time.time()
            key = "ollama:circuit_breaker:failures"
            await asyncio.to_thread(r.zadd, key, {str(now): now})
            await asyncio.to_thread(r.zremrangebyscore, key, "-inf", now - 60)
            count = await asyncio.to_thread(r.zcard, key)
            if count >= 3:
                await asyncio.to_thread(r.set, "ollama:circuit_breaker:blackout", "1", ex=300)
                logger.warning("[InferenceScheduler] Circuit breaker tripped! 3 fails in 60s. Blackout active for 300s.")
        except Exception as e:
            logger.warning(f"[InferenceScheduler] Error in circuit breaker record: {e}")

    async def execute(self, juror_spec: dict, prompt_text: str, timeout: int, system_prompt: str = None) -> Optional[str]:
        model_name = juror_spec.get("model", "")
        
        # 1. Cloud models (Gemini, OpenAI, Cerebras, SambaNova) run immediately without scheduling
        info = ModelFootprints.get_info(model_name)
        is_cloud = (
            juror_spec.get("api_key") != "ollama"
            or info is None
            or any(ind in model_name.lower() for ind in ["gemini", "openai", "claude", "cerebras", "sambanova"])
        )
        
        if is_cloud:
            logger.info(f"[InferenceScheduler] Cloud model {model_name} detected. Executing immediately.")
            return await self._make_http_call(juror_spec, prompt_text, timeout, system_prompt)

        # Local model logic
        host = info["host"]
        tier = info["tier"]
        cold_load = info.get("cold_load", 30)

        # Check circuit breaker
        if await self._is_circuit_breaker_active():
            logger.warning(f"[InferenceScheduler] Circuit breaker active. Routing {model_name} to fallback.")
            return await self._execute_fallback(juror_spec, prompt_text, timeout, system_prompt, reason="circuit_breaker_active")

        # Preflight check before locks
        base_url = ModelFootprints.HOSTS.get(host, "http://localhost:11434/v1")
        if not await self._ollama_alive(base_url):
            logger.warning(f"[InferenceScheduler] Preflight check failed for {base_url}. Routing {model_name} to fallback.")
            await self._record_failure()
            return await self._execute_fallback(juror_spec, prompt_text, timeout, system_prompt, reason="preflight_failed")

        # 2. Check host online status via 'ollama:health' Redis key
        host_online = True
        r = self._get_redis()
        if r:
            try:
                health_str = await asyncio.to_thread(r.get, "ollama:health")
                if health_str:
                    health_data = json.loads(health_str)
                    if host == "studio":
                        host_online = health_data.get("local_online", False)
                    elif host == "pro":
                        host_online = health_data.get("remote_online", False)
            except Exception as e:
                logger.warning(f"[InferenceScheduler] Error reading ollama:health: {e}")

        if not host_online:
            logger.warning(f"[InferenceScheduler] Host {host} is offline. Routing {model_name} to fallback.")
            return await self._execute_fallback(juror_spec, prompt_text, timeout, system_prompt, reason="host_offline")

        # 3. Advisory Locking for heavy and medium tiers
        acquired = False
        lock_key = f"ollama:lock:{host}:heavy"
        
        if tier in ("heavy", "medium"):
            ttl = cold_load + timeout
            start_time = time.time()
            backoff = 0.5
            
            logger.info(f"[InferenceScheduler] Acquiring advisory lock {lock_key} for {model_name} (tier={tier}).")
            while time.time() - start_time < 180:
                if r:
                    try:
                        # Attempt to acquire lock atomically
                        acquired = await asyncio.to_thread(r.set, lock_key, "1", ex=ttl, nx=True)
                        if acquired:
                            logger.info(f"[InferenceScheduler] Lock {lock_key} acquired successfully for {model_name}.")
                            break
                    except Exception as e:
                        logger.warning(f"[InferenceScheduler] Redis locking failed, will retry: {e}")
                else:
                    logger.warning("[InferenceScheduler] Redis unavailable for advisory locking. Bypassing lock.")
                    acquired = True
                    break
                
                await asyncio.sleep(backoff)
                backoff = min(backoff * 1.5, 3.0)

            if not acquired:
                logger.warning(f"[InferenceScheduler] Lock acquisition timed out for {model_name} after 180s. Tripping circuit breaker and falling back.")
                await self._record_failure()
                return await self._execute_fallback(juror_spec, prompt_text, timeout, system_prompt, reason="lock_timeout")

        # 4. Execute standard local call with finally block to release lock
        try:
            logger.info(f"[InferenceScheduler] Executing local model {model_name} on {host}.")
            return await self._make_http_call(juror_spec, prompt_text, timeout, system_prompt)
        except Exception as e:
            logger.warning(f"[InferenceScheduler] Local execution of {model_name} failed: {type(e).__name__}: {e!r}. Executing fallback.")
            await self._record_failure()
            return await self._execute_fallback(juror_spec, prompt_text, timeout, system_prompt, reason=f"execution_error: {type(e).__name__}: {e!r}")
        finally:
            if acquired and r:
                async def _release():
                    try:
                        await asyncio.wait_for(
                            asyncio.to_thread(r.delete, lock_key),
                            timeout=2.0
                        )
                        logger.info(f"[InferenceScheduler] Released lock {lock_key} for {model_name}.")
                    except Exception as err:
                        logger.warning(f"[InferenceScheduler] Failed to release lock {lock_key}: {type(err).__name__}: {err!r}")
                try:
                    await asyncio.shield(_release())
                except Exception as err:
                    logger.warning(f"[InferenceScheduler] Shielded release lock wrapper exception: {type(err).__name__}: {err!r}")

    async def _execute_fallback(self, juror_spec: dict, prompt_text: str, timeout: int, system_prompt: str = None, reason: str = "") -> Optional[str]:
        model_name = juror_spec.get("model", "")
        logger.warning(f"[InferenceScheduler] Fallback triggered for {model_name}. Reason: {reason}")
        
        info = ModelFootprints.get_info(model_name)
        target_host = info["host"] if info else "studio"
        
        fallback_spec = None
        
        # Determine fallback model spec
        if settings.GEMINI_API_KEY:
            fallback_spec = {
                "model": BATCH_SAFE_DEFAULT_MODEL or "gemini-2.5-flash",
                "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
                "api_key": settings.GEMINI_API_KEY,
                "label": f"{juror_spec.get('label', '')}-Fallback-Gemini",
                "max_tokens": 8192
            }
        elif settings.OLLAMA_STUDIO_FAST_MODEL:
            fallback_spec = {
                "model": settings.OLLAMA_STUDIO_FAST_MODEL,
                "base_url": settings.OLLAMA_STUDIO_BASE_URL or "http://localhost:11434/v1",
                "api_key": "ollama",
                "label": f"{juror_spec.get('label', '')}-Fallback-Local"
            }
        else:
            fallback_spec = {
                "model": "gpt-oss:20b",
                "base_url": "http://localhost:11434/v1",
                "api_key": "ollama",
                "label": f"{juror_spec.get('label', '')}-Fallback-Local"
            }
            
        logger.info(f"[InferenceScheduler] Falling back from {model_name} to {fallback_spec['model']}")
        fallback_base = fallback_spec.get("base_url") or ""
        if (
            fallback_spec.get("api_key") == "ollama"
            and _is_local_url(fallback_base)
            and any(marker in reason for marker in ("preflight_failed", "host_offline", "circuit_breaker_active"))
        ):
            logger.warning(
                "[InferenceScheduler] Skipping local fallback %s after unhealthy-local reason=%s",
                fallback_spec["model"],
                reason,
            )
            return None

        fallback_timeout = min(int(timeout), FALLBACK_TIMEOUT_SECONDS)
        try:
            return await self._make_http_call(fallback_spec, prompt_text, fallback_timeout, system_prompt)
        except Exception as e:
            logger.error(f"[InferenceScheduler] Fallback execution failed: {e}")
            return None

    async def _make_http_call(self, juror_spec: dict, prompt_text: str, timeout: int, system_prompt: str = None) -> str:
        model_name = juror_spec["model"]
        if juror_spec.get("no_think"):
            prompt_text = f"/no_think\n{prompt_text}"
            if system_prompt:
                system_prompt = f"{system_prompt}\n\nDo not think step by step. Return only the requested JSON."
            else:
                system_prompt = "Do not think step by step. Return only the requested JSON."
        
        if "deepseek-r1" in model_name.lower():
            if system_prompt:
                messages = [
                    {"role": "user", "content": f"{system_prompt}\n\n{prompt_text}"}
                ]
            else:
                messages = [
                    {"role": "user", "content": prompt_text}
                ]
        else:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt_text})

        payload = {
            "model": model_name,
            "messages": messages,
            "stream": False,
        }
        
        if "temperature" in juror_spec:
            payload["temperature"] = juror_spec["temperature"]
        if "max_tokens" in juror_spec:
            payload["max_tokens"] = juror_spec["max_tokens"]
        if juror_spec.get("no_think"):
            payload["thinking"] = False
            payload["think"] = False
            payload["reasoning_effort"] = "none"
            
        base_url = juror_spec.get("base_url") or "http://localhost:11434/v1"
        is_local_ollama = juror_spec.get("api_key") == "ollama" and _is_local_url(base_url)

        if is_local_ollama:
            payload["options"] = {"num_ctx": int(juror_spec.get("num_ctx", 8192))}
            if "temperature" in juror_spec:
                payload["options"]["temperature"] = juror_spec["temperature"]
            if "num_predict" in juror_spec:
                payload["options"]["num_predict"] = juror_spec["num_predict"]

        headers = {}
        api_key = juror_spec.get("api_key") or ""
        if api_key and api_key != "ollama":
            headers["Authorization"] = f"Bearer {api_key}"

        if is_local_ollama:
            # Ollama's OpenAI-compatible endpoint can ignore model context settings
            # from the payload for some Modelfiles. Use the native chat API so
            # num_ctx=8192 is enforced at runner load time.
            ollama_root = base_url.rstrip("/").removesuffix("/v1")
            url = f"{ollama_root}/api/chat"
        else:
            url = f"{base_url.rstrip('/')}/chat/completions"

        async def _do_call():
            request_timeout = _http_timeout(float(timeout))
            if is_local_ollama:
                # Local Ollama runner sockets can get wedged after model-load failures.
                # Use a fresh client per generation so cancellation closes the socket.
                async with httpx.AsyncClient(timeout=request_timeout) as client:
                    response = await client.post(url, json=payload)
            else:
                client = get_persistent_client()
                response = await client.post(
                    url,
                    headers=headers,
                    json=payload,
                    timeout=request_timeout,
                )
            response.raise_for_status()
            data = response.json()

            if is_local_ollama:
                content = (data.get("message") or {}).get("content") or data.get("response") or ""
                return clean_llm_response(content)

            choices = data.get("choices", [])
            if choices:
                message = choices[0].get("message", {})
                content = message.get("content", "")
                return clean_llm_response(content)
            return ""

        try:
            return await asyncio.wait_for(_do_call(), timeout=float(timeout))
        except asyncio.TimeoutError:
            logger.warning(f"[InferenceScheduler] HTTP call timed out (wall-clock) after {timeout}s")
            raise
