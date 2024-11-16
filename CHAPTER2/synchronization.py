import threading
import time
from concurrent.futures import ThreadPoolExecutor

sem = threading.Semaphore(1)

def access_resource(thread_name):
    with sem:
        print(f"{thread_name} accessing the resource")
        time.sleep(1)
        print(f"{thread_name} done")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            executor.submit(access_resource, f"Thread-{i}")
