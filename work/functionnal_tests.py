import warnings
warnings.filterwarnings('ignore')
import requests
import time

def get_pinged(url, nb_ping):
    start_time = time.time()
    urls = [url] * nb_ping
    for i in urls:
        requests.get(i)
    return ((time.time() - start_time) / nb_ping)


def test_status():
    assert requests.get("http://localhost:5000").status_code == 200

def test_stresstest():
    assert get_pinged("http://127.0.0.1:5000", 100) <= 0.1