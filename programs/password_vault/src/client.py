from solana.rpc.async_api import AsyncClient

async def main():
    client = AsyncClient("http://localhost:8899")
    # тут твій код для взаємодії з контрактом

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
