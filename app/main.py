import asyncio
from app import FastAPIServer


async def main():
    await FastAPIServer().run()


if __name__ == "__main__":
    asyncio.run(main())
