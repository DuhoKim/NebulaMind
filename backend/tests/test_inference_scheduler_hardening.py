import asyncio
import time
import pytest
import httpx
from unittest.mock import AsyncMock, MagicMock, patch
from app.services.inference_scheduler import (
    InferenceScheduler,
    get_persistent_client,
    _OLLAMA_LIVENESS_CACHE,
)

@pytest.mark.anyio
async def test_get_persistent_client():
    client = get_persistent_client()
    assert isinstance(client, httpx.AsyncClient)
    # Check that transport has limits and socket options
    transport = client._transport
    assert transport is not None
    assert hasattr(transport, "_pool")

@pytest.mark.anyio
async def test_ollama_alive_probe(monkeypatch):
    scheduler = InferenceScheduler()
    base_url = "http://localhost:11434/v1"
    
    # Reset cache
    _OLLAMA_LIVENESS_CACHE.clear()
    
    # Mock persistent client's get method
    mock_get = AsyncMock()
    mock_get.return_value.status_code = 200
    
    with patch("app.services.inference_scheduler.get_persistent_client") as mock_client_factory:
        mock_client = MagicMock()
        mock_client.get = mock_get
        mock_client_factory.return_value = mock_client
        
        alive = await scheduler._ollama_alive(base_url)
        assert alive is True
        mock_get.assert_called_once_with("http://localhost:11434/api/tags", timeout=0.5)

@pytest.mark.anyio
async def test_circuit_breaker_blackout(monkeypatch):
    scheduler = InferenceScheduler()
    
    # Mock Redis client
    mock_redis = MagicMock()
    mock_redis.get.return_value = "1"  # simulated blackout key active
    
    # Inject mock Redis into the scheduler
    scheduler._redis = mock_redis
    
    active = await scheduler._is_circuit_breaker_active()
    assert active is True

@pytest.mark.anyio
async def test_circuit_breaker_tripping(monkeypatch):
    scheduler = InferenceScheduler()
    mock_redis = MagicMock()
    scheduler._redis = mock_redis
    
    zcard_val = 0
    async def mock_zadd(key, val):
        pass
    async def mock_zremrangebyscore(key, min_val, max_val):
        pass
    async def mock_zcard(key):
        nonlocal zcard_val
        return zcard_val
    async def mock_set(key, val, ex=None, nx=False):
        pass

    # We mock asyncio.to_thread calls
    original_to_thread = asyncio.to_thread
    async def mock_to_thread(func, *args, **kwargs):
        if func == mock_redis.zadd:
            return await mock_zadd(*args, **kwargs)
        elif func == mock_redis.zremrangebyscore:
            return await mock_zremrangebyscore(*args, **kwargs)
        elif func == mock_redis.zcard:
            return await mock_zcard(*args, **kwargs)
        elif func == mock_redis.set:
            return await mock_set(*args, **kwargs)
        return await original_to_thread(func, *args, **kwargs)
        
    monkeypatch.setattr(asyncio, "to_thread", mock_to_thread)
    
    # Test recording failure triggers blackout when fails >= 3
    zcard_val = 3
    # Set up spy on mock_redis.set
    set_called_with = []
    async def spy_set(key, val, ex=None, nx=False):
        set_called_with.append((key, val, ex))
    mock_set = spy_set
    
    await scheduler._record_failure()
    assert len(set_called_with) > 0
    assert set_called_with[0][0] == "ollama:circuit_breaker:blackout"
    assert set_called_with[0][1] == "1"
    assert set_called_with[0][2] == 300

@pytest.mark.anyio
async def test_make_http_call_timeout(monkeypatch):
    scheduler = InferenceScheduler()
    juror_spec = {
        "model": "qwen3:30b",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama"
    }
    
    # Mock get_persistent_client to hang
    async def slow_post(*args, **kwargs):
        await asyncio.sleep(5.0)
        return MagicMock()
        
    with patch("app.services.inference_scheduler.get_persistent_client") as mock_client_factory:
        mock_client = MagicMock()
        mock_client.post = slow_post
        mock_client_factory.return_value = mock_client
        
        # Expect TimeoutError within 1 second
        with pytest.raises(asyncio.TimeoutError):
            await scheduler._make_http_call(juror_spec, "test prompt", timeout=1)
