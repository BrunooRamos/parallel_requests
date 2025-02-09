import multiprocessing
import requests
import time

URL = "https://httpbin.org/get"
N_REQUESTS = 10

def fetch(i):
    response = requests.get(URL)
    return f"Request {i}: Status {response.status_code}, Time {response.elapsed.total_seconds()}s"

def main():
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:  # Usa 4 procesos reales
        results = pool.map(fetch, range(N_REQUESTS))
    
    total_time = time.time() - start_time
    print("\n".join(results))
    print(f"\nTotal time with multiprocessing: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
