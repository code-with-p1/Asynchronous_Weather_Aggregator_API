import time
from typing import List
import aiohttp
import requests  # Added for synchronous HTTP requests
from fastapi import FastAPI
import asyncio

app = FastAPI()

# List of cities for demonstration
CITIES = ["London", "New York", "Tokyo", "Sydney", "Paris"]

# External API endpoint (Open-Meteo: free, no key needed)
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

# City coordinates (hardcoded for simplicity)
CITY_COORDS = {
    "London": {"lat": 51.5074, "lon": -0.1278},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Tokyo": {"lat": 35.6895, "lon": 139.6917},
    "Sydney": {"lat": -33.8688, "lon": 151.2093},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
}

async def fetch_weather(session: aiohttp.ClientSession, city: str) -> dict:
    coords = CITY_COORDS.get(city)
    if not coords:
        return {city: "Invalid city"}
    
    url = WEATHER_API_URL.format(lat=coords["lat"], lon=coords["lon"])
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return {city: data.get("current_weather", "No data")}
        return {city: f"Error: {response.status}"}

# Async endpoint: Fetches weather for all cities concurrently
@app.get("/weather/async")
async def get_weather_async():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city) for city in CITIES]
        results = await asyncio.gather(*tasks)  # Run all fetches concurrently
    duration = time.time() - start_time
    return {
        "method": "async",
        "duration": f"{duration:.2f} seconds",
        "data": {k: v for result in results for k, v in result.items()}
    }

# Sync endpoint: Fetches weather for all cities sequentially
@app.get("/weather/sync")
def get_weather_sync():
    start_time = time.time()
    results = []
    for city in CITIES:
        coords = CITY_COORDS.get(city)
        if not coords:
            results.append({city: "Invalid city"})
            continue
        url = WEATHER_API_URL.format(lat=coords["lat"], lon=coords["lon"])
        response = requests.get(url)  # Synchronous HTTP request
        if response.status_code == 200:
            data = response.json()
            results.append({city: data.get("current_weather", "No data")})
        else:
            results.append({city: f"Error: {response.status_code}"})
    duration = time.time() - start_time
    return {
        "method": "sync",
        "duration": f"{duration:.2f} seconds",
        "data": {k: v for result in results for k, v in result.items()}
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("weather_api:app", host="127.0.0.1", port=8000, reload=True)