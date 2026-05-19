"""
Astronomical Data Scraper
Fetches astronomical observation data from public sources
"""

import requests
import csv
from datetime import datetime
from pathlib import Path
import json

# Create data directory if it doesn't exist
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def scrape_space_weather():
    """Fetch space weather data from NOAA"""
    print("Fetching space weather data...")
    try:
        url = "https://services.swpc.noaa.gov/products/space-weather-observations.json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"✓ Retrieved {len(data)} space weather observations")
        return data
    except Exception as e:
        print(f"✗ Error fetching space weather: {e}")
        return []

def scrape_asteroid_data():
    """
    Fetch near-Earth asteroid data from NASA
    Note: This requires an API key from https://api.nasa.gov/
    For now, we'll create sample data
    """
    print("Generating sample asteroid data...")
    sample_asteroids = [
        {
            "name": "2024 AB1",
            "distance_km": 450000,
            "velocity_kms": 18.5,
            "size_m": 145,
            "hazard": False
        },
        {
            "name": "2024 CD5",
            "distance_km": 1200000,
            "velocity_kms": 22.3,
            "size_m": 89,
            "hazard": False
        },
        {
            "name": "2023 XY7",
            "distance_km": 800000,
            "velocity_kms": 19.8,
            "size_m": 256,
            "hazard": False
        },
    ]
    print(f"✓ Generated {len(sample_asteroids)} asteroid observations")
    return sample_asteroids

def save_observations_to_csv(asteroids):
    """Save asteroid observations to CSV file"""
    if not asteroids:
        print("✗ No data to save")
        return
    
    csv_path = DATA_DIR / "asteroids_observations.csv"
    try:
        with open(csv_path, "w", newline="") as csvfile:
            fieldnames = ["name", "distance_km", "velocity_kms", "size_m", "hazard", "observation_date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for asteroid in asteroids:
                row = asteroid.copy()
                row["observation_date"] = datetime.now().isoformat()
                writer.writerow(row)
        
        print(f"✓ Saved observations to {csv_path}")
    except Exception as e:
        print(f"✗ Error saving to CSV: {e}")

def save_space_weather_to_json(data):
    """Save space weather data to JSON file"""
    if not data:
        print("✗ No space weather data to save")
        return
    
    json_path = DATA_DIR / "space_weather.json"
    try:
        with open(json_path, "w") as jsonfile:
            json.dump(data[:10], jsonfile, indent=2)  # Save first 10 observations
        print(f"✓ Saved space weather data to {json_path}")
    except Exception as e:
        print(f"✗ Error saving JSON: {e}")

def main():
    """Main scraper function"""
    print("=" * 50)
    print("Astronomical Data Scraper")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Scrape data
    space_weather = scrape_space_weather()
    asteroids = scrape_asteroid_data()
    
    # Save data
    if asteroids:
        save_observations_to_csv(asteroids)
    
    if space_weather:
        save_space_weather_to_json(space_weather)
    
    print("=" * 50)
    print("Scraping complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()
