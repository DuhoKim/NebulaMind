import httpx
import asyncio

async def test():
    url = "http://192.188.0.4:11435/v1/chat/completions"
    payload = {
        "model": "deepseek-r1:32b",
        "messages": [
            {"role": "system", "content": "hello system"},
            {"role": "user", "content": "hello user"},
        ],
        "stream": False,
        "temperature": 0,
        "options": {"num_ctx": 4096, "temperature": 0},
    }
    
    async with httpx.AsyncClient() as client:
        try:
            print("Sending POST request to Buddle...")
            res = await client.post(url, json=payload, timeout=45)
            print("Response status:", res.status_code)
            print("Response headers:", res.headers)
            print("Response text:", res.text[:200])
        except Exception as e:
            print("Exception raised:")
            import traceback
            traceback.print_exc()

asyncio.run(test())
