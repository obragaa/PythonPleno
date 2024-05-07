import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://jsonplaceholder.typicode.com/todos/"
    content = await fetch(url)
    print(content[:200])  # Imprime os primeiros 200 caracteres da resposta

asyncio.run(main())
