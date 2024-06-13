import requests
from config import HEADERS


def fetch_url(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  # Ensure we notice bad responses
    return response.text
