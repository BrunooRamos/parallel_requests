import requests
import concurrent.futures
import time

URL = "https://httpbin.org/get"
N_REQUESTS = 10  # Número de peticiones simultáneas

def fetch(i):
    response = requests.get(URL)
    return f"Request {i}: Status {response.status_code}, Time {response.elapsed.total_seconds()}s"

def main():
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch, range(N_REQUESTS)))
    
    total_time = time.time() - start_time
    
    print("\n".join(results))
    print(f"\nTotal time with ThreadPoolExecutor: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()


# Ver aca la documentacion de threads: https://realpython.com/intro-to-python-threading/#using-a-threadpoolexecutor