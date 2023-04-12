import aioredis
from aioredis import Redis, Connection
def RedInjection(host: str, port: int, db: int, minsize: int, maxsize: int, encoding: str, decode_responses: bool):
    def back(cls):
        cls.host = host
        cls.port = port
        cls.db = db
        cls.minsize = minsize
        cls.maxsize = maxsize
        cls.encoding = encoding
        cls.decode_responses = decode_responses
        return cls

    return back


class XRed:
    def __init__(self):
        self.pool:Redis
    async def create_pool(self):
        self.pool = await aioredis.from_url(
            "redis://127.0.0.1", port=12008, db=0, encoding="utf-8", decode_responses=True,
        )

    async def close_pool(self):
        if self.pool:
            pass
        else:
            await self.pool.close()