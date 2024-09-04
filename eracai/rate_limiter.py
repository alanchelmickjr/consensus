import asyncio
from .models.config import Config

class RateLimiter:
    def __init__(self, rate_limit):
        self.rate_limit = rate_limit
        self.tokens = rate_limit
        self.updated_at = asyncio.get_event_loop().time()

    async def acquire(self):
        now = asyncio.get_event_loop().time()
        time_passed = now - self.updated_at
        self.tokens = min(self.rate_limit, self.tokens + time_passed * self.rate_limit)
        self.updated_at = now

        if self.tokens < 1:
            await asyncio.sleep(1)
            return await self.acquire()
        
        self.tokens -= 1
        return True

async def with_retries(func, *args, **kwargs):
    for attempt in range(Config.MAX_RETRIES):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            if attempt == Config.MAX_RETRIES - 1:
                raise
            await asyncio.sleep(2 ** attempt)  # Exponential backoff