import asyncio
import httpx
import time

URL = "https://httpbin.org/get"
N_REQUESTS = 10  # Número de peticiones simultáneas

async def fetch(client, i):
    response = await client.get(URL)
    return f"Request {i}: Status {response.status_code}, Time {response.elapsed.total_seconds()}s"

async def main():
    start_time = time.time()

    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, i) for i in range(N_REQUESTS)]
        results = await asyncio.gather(*tasks)
    
    total_time = time.time() - start_time
    
    print("\n".join(results))
    print(f"\nTotal time with httpx (asyncio): {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())


# Ver aca la documentacion de httpx: https://www.python-httpx.org/
# Ver aca la documentacion de async: https://www.python-httpx.org/async/