import warnings
warnings.filterwarnings('ignore')

import urllib.request

def fetching(input):
    urllib.request.Request('http://localhost:5000/sentiment?message='+input)
    return True

def test_fetch():
    assert fetching('fetch') == True