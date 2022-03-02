import warnings
warnings.filterwarnings('ignore')
import requests
import time

def get_pinged():
    start_time = time.time()
    urls = ["http://localhost:5000"] * 100
    for i in urls:
        requests.get(i)
    return ((time.time() - start_time) / 100)


def test_status():
    assert requests.get("http://localhost:5000").status_code == 200

def stress_test():
    assert get_pinged() <= 0.1