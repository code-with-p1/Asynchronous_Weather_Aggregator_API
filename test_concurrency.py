import concurrent.futures
import requests
import time

URL = "http://127.0.0.1:8000/weather/async"  # Change to /sync for comparison
NUM_REQUESTS = 10  # Simulate 10 concurrent users

def make_request():
    start = time.time()
    response = requests.get(URL)
    duration = time.time() - start
    return response.json(), duration

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(lambda _: make_request(), range(NUM_REQUESTS)))
total_duration = time.time() - start_time

print(f"Total time for {NUM_REQUESTS} concurrent requests: {total_duration:.2f} seconds")
for i, (data, dur) in enumerate(results):
    print(f"Request {i+1}: Duration {dur:.2f}s, Method: {data['method']}")