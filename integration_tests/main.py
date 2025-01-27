import time
import requests


BASE_URL = "http://web:8000"


def _request(method, endpoint, data=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.request(method, url, json=data)
    return response


def test_close_claim():
    response = _request("POST", "claims", {})
    assert response.status_code == 201
    assert response.json()["claim_uuid"] is not None    claims = response.json()["claims"]
    assert claim_under_test["closed"] == True


def test_assign_claim_to_adjuster():
    response = _request("POST", "claims", {})
    assert response.status_code == 201
    assert response.json()["claim_uuid"] is not None    claims = response.json()["claims"]
    assert claim_under_test["closed"] == True


