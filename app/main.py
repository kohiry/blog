import asyncio
from app import FastAPIServer


async def main():
    servers = [
        FastAPIServer(),
    ]
    await asyncio.gather(*map(lambda server: server.run(), servers))


if __name__ == "__main__":
    asyncio.run(main())
