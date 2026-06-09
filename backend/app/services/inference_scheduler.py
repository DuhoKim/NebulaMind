import json
import time
import asyncio
import logging
import httpx
import redis
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
        "llama3.1:405b": {
            "host": "pro",
            "tier": "heavy",
            "vram_gb": 344,
            "slots": 1,
            "cold_load": 120
        },
        "llama3.3:70b": {
            "host": "studio",
            "tier": "heavy",
            "vram_gb": 42,
            "slots": 1,
            "cold_load": 30
        },
        "deepseek-r1:70b": {
            "host": "studio",
            "tier": "heavy",
            "vram_gb": 42,
            "slots": 1,
            "cold_load": 30
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
        "qwen3:30b": {
            "host": "studio",
            "tier": "medium",
            "vram_gb": 18,
            "slots": 1,
            "cold_load": 15
        },
        "qwen3:30b-a3b-instruct-2507-q4_K_M": {
            "host": "studio",
            "tier": "medium",
            "vram_gb": 18,
            "slots": 1,
            "cold_load": 15
        },
        "deepseek-r1:14b": {
            "host": "studio",
            "tier": "light",
            "vram_gb": 9,
            "slots": 0,
            "cold_load": 5
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

    async def execute(self, juror_spec: dict, prompt_text: str, timeout: int, system_prompt: str = None) -> Optional[str]:
        model_name = juror_spec.get("model", "")
        
        # 1. Cloud models (Gemini, OpenAI, Cerebras, SambaNova) run immediately without scheduling
        info = ModelFootprints.get_info(model_name)
        is_cloud = (
            info is None or 
            any(ind in model_name.lower() for ind in ["gemini", "gpt", "openai", "claude", "cerebras", "sambanova"]) or
            juror_spec.get("api_key") != "ollama"
        )
        
        if is_cloud:
            logger.info(f"[InferenceScheduler] Cloud model {model_name} detected. Executing immediately.")
            return await self._make_http_call(juror_spec, prompt_text, timeout, system_prompt)

        # Local model logic
        host = info["host"]
        tier = info["tier"]
        cold_load = info.get("cold_load", 30)

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
            # Raised wait from 30s to 240s to allow heavy local model serialization
            # (e.g. Mima 30B takes ~45s, so Buddle 70B needs to wait ~45s in queue cleanly).
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
                logger.warning(f"[InferenceScheduler] Lock acquisition timed out for {model_name} after 30s. Tripping circuit breaker and falling back.")
                return await self._execute_fallback(juror_spec, prompt_text, timeout, system_prompt, reason="lock_timeout")

        # 4. Execute standard local call with finally block to release lock
        try:
            logger.info(f"[InferenceScheduler] Executing local model {model_name} on {host}.")
            return await self._make_http_call(juror_spec, prompt_text, timeout, system_prompt)
        except Exception as e:
            logger.warning(f"[InferenceScheduler] Local execution of {model_name} failed: {e}. Executing fallback.")
            return await self._execute_fallback(juror_spec, prompt_text, timeout, system_prompt, reason=f"execution_error: {e}")
        finally:
            if acquired and r:
                try:
                    await asyncio.to_thread(r.delete, lock_key)
                    logger.info(f"[InferenceScheduler] Released lock {lock_key} for {model_name}.")
                except Exception as e:
                    logger.warning(f"[InferenceScheduler] Failed to release lock {lock_key}: {e}")

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
                "model": "deepseek-r1:14b",
                "base_url": "http://localhost:11434/v1",
                "api_key": "ollama",
                "label": f"{juror_spec.get('label', '')}-Fallback-Local"
            }
            
        logger.info(f"[InferenceScheduler] Falling back from {model_name} to {fallback_spec['model']}")
        try:
            return await self._make_http_call(fallback_spec, prompt_text, timeout, system_prompt)
        except Exception as e:
            logger.error(f"[InferenceScheduler] Fallback execution failed: {e}")
            return None

    async def _make_http_call(self, juror_spec: dict, prompt_text: str, timeout: int, system_prompt: str = None) -> str:
        model_name = juror_spec["model"]
        
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
            
        if juror_spec.get("api_key") == "ollama" or "localhost" in juror_spec.get("base_url", "") or "127.0.0.1" in juror_spec.get("base_url", ""):
            payload["options"] = {"num_ctx": 8192}
            if "temperature" in juror_spec:
                payload["options"]["temperature"] = juror_spec["temperature"]

        headers = {}
        api_key = juror_spec.get("api_key") or ""
        if api_key and api_key != "ollama":
            headers["Authorization"] = f"Bearer {api_key}"

        base_url = juror_spec.get("base_url") or "http://localhost:11434/v1"
        url = f"{base_url.rstrip('/')}/chat/completions"

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                headers=headers,
                json=payload,
                timeout=timeout,
            )
            response.raise_for_status()
            data = response.json()
            
            choices = data.get("choices", [])
            if choices:
                message = choices[0].get("message", {})
                content = message.get("content", "")
                return clean_llm_response(content)
            return ""
