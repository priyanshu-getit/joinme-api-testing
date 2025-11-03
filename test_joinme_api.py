import requests
import pytest
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"

def test_api_status():
    res = requests.get(API_URL)
    assert res.status_code == 200, f"Got {res.status_code}"

def test_response_time():
    res = requests.get(API_URL)
    assert res.elapsed.total_seconds() < 2, "API too slow"

def test_json_structure():
    res = requests.get(API_URL)
    data = res.json()
    assert isinstance(data, list)
    assert "title" in data[0] and "body" in data[0]

def test_no_sensitive_data():
    res = requests.get(API_URL)
    body = res.text.lower()
    assert "password" not in body and "token" not in body
