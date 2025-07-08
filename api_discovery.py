# api_discovery.py
import requests
from typing import List, Dict

def discover_free_apis(limit: int = 10) -> List[Dict]:
    """
    Fetches a list of free public APIs from the Public APIs directory.
    Filters for APIs that require no authentication and support HTTPS.
    """
    try:
        response = requests.get("https://api.publicapis.org/entries", timeout=10)
        response.raise_for_status()
        data = response.json()
        free_apis = [
            {
                "name": entry["API"],
                "description": entry["Description"],
                "link": entry["Link"],
                "category": entry["Category"]
            }
            for entry in data["entries"]
            if entry["Auth"] == "" and entry["HTTPS"]
        ]
        return free_apis[:limit]
    except Exception as e:
        print(f"API discovery failed: {e}")
        return []
