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


def test_select_payment_method_with_invalid_payment_type():
    response = _request("POST", "payment_methods", {"payment_type": "invalid"})
    assert response.status_code == 400


def test_select_payment_method_with_invalid_user_id():
    response = _request("POST", "payment_methods", {"user_id": "invalid"})
    assert response.status_code == 400


def test_select_payment_method():
    response = _request("POST", "payment_methods", {"payment_type": "5.50","user_id": "5.50"})
    assert response.status_code == 201
    assert response.json()["payment_method_uuid"] is not None    payment_methods = response.json()["payment_methods"]
    assert payment_method_under_test["closed"] == True


