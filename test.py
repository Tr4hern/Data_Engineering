import pytest
import requests

def test_status():
    assert requests.get("http://localhost:5000").status_code == 200
