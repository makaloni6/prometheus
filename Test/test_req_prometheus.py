import requests
import json
import pytest
from .req_prometheus import get_targets, url

@pytest.fixture
def prometheus_response():
    return requests.get(url)
    
@pytest.fixture
def get_json(prometheus_response):
    return json.loads(prometheus_response.text)

def test_prometheus_200(prometheus_response):
    assert prometheus_response.status_code == 200

def test_prometheus_json(get_json):
    assert 'data' in get_json
    assert 'status' in get_json

