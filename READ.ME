# Asynchronous Weather Aggregator API

This project demonstrates the power of asynchronous programming in Python using **FastAPI** and **aiohttp**. It implements a weather aggregator API that fetches current weather data for multiple cities from the [Open-Meteo API](https://open-meteo.com/) (no API key required). The project compares **asynchronous** and **synchronous** endpoints to highlight how async handles multiple requests concurrently, improving performance for I/O-bound tasks like HTTP requests.

## Features
- **Async Endpoint**: Fetches weather data for multiple cities concurrently using `aiohttp` and `asyncio.gather`.
- **Sync Endpoint**: Fetches weather data sequentially using `requests` for comparison.
- **Concurrency Testing**: Includes a script to simulate multiple simultaneous requests, showcasing async's scalability.
- **Real-World Use Case**: Mimics a travel app fetching weather for multiple destinations, demonstrating I/O-bound task handling.

## Prerequisites
- **Python**: 3.8 or higher
- **Dependencies**:
  - `fastapi`: Web framework for building the API
  - `uvicorn`: ASGI server to run the API
  - `aiohttp`: Async HTTP client for the async endpoint
  - `requests`: Sync HTTP client for the sync endpoint

## Setup
1. **Clone or Create the Project**:
   - Create a directory for the project (e.g., `weather_api_project`).
   - Save the main code in a file named `weather_api.py` (see the project code provided earlier).

2. **Install Dependencies**:
   Run the following command in your terminal:
   ```bash
   pip install fastapi uvicorn aiohttp requests
   ```

3. **Verify Python Version**:
   Ensure Python 3.8+ is installed:
   ```bash
   python --version
   ```

## Running the API
1. Navigate to the project directory containing `weather_api.py`.
2. Start the FastAPI server:
   ```bash
   python weather_api.py
   ```
3. The server will run on `http://127.0.0.1:8000`. Access the interactive Swagger UI at `http://127.0.0.1:8000/docs` to test endpoints.

## Endpoints
- **Async Endpoint**: `GET /weather/async`
  - Fetches weather data for multiple cities concurrently.
  - Example: `curl http://127.0.0.1:8000/weather/async`
  - Response includes execution time and weather data for cities like London, New York, Tokyo, etc.
- **Sync Endpoint**: `GET /weather/sync`
  - Fetches weather data sequentially for comparison.
  - Example: `curl http://127.0.0.1:8000/weather/sync`
  - Response shows longer execution time due to blocking calls.

## Testing Concurrency
To compare async vs. sync performance under concurrent requests:
1. Save the following script as `test_concurrency.py`:
   ```python
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
   ```
2. Run the script:
   ```bash
   python test_concurrency.py
   ```
3. **Observations**:
   - **Async**: Total time is close to a single request’s duration (e.g., ~1-2s for 10 requests), as requests are handled concurrently.
   - **Sync**: Total time is much longer (e.g., ~5-10s), as each request blocks the server.

## How It Demonstrates Async
- **Async Advantage**: The `/weather/async` endpoint uses `asyncio.gather` to fetch weather data concurrently, minimizing wait time for I/O-bound HTTP requests.
- **Sync Limitation**: The `/weather/sync` endpoint fetches data sequentially, blocking the thread for each request, which slows down under load.
- **Scalability**: Async allows the server to handle multiple simultaneous requests efficiently, ideal for real-world APIs with high traffic.

## Troubleshooting
- **Port Conflict**: If `port 8000` is in use, change the port in `weather_api.py` (e.g., `uvicorn.run(app, host="127.0.0.1", port=8001)`).
- **API Errors**: If the Open-Meteo API fails, check your internet connection or try different cities.
- **Dependency Issues**: Ensure all dependencies are installed (`pip install fastapi uvicorn aiohttp requests`).
- **Logs**: Add `print` statements in `weather_api.py` (e.g., `print(f"Fetching {city}")`) to debug execution flow.

## Extending the Project
- **Add a Database**: Use `aiosqlite` for async database operations to cache weather data.
- **Error Handling**: Add try-except blocks to handle API failures.
- **More Cities**: Expand the `CITIES` list to test performance with more data.
- **Load Testing**: Use tools like `locust` or `ab` for advanced load testing.

## License
This project is for educational purposes and uses the Open-Meteo API, which is freely available. Ensure compliance with their terms if used in production.
