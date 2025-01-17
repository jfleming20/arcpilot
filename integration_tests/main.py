import time
import requests


BASE_URL = "http://web:8000"


def _request(method, endpoint, data=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.request(method, url, json=data)
    return response


