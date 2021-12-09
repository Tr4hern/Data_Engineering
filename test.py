import pytest
import requests
import app

def test_status():
    assert requests.get("http://localhost:5000").status_code == 200

def test_sentiment():
    assert app.vader_analyse("I love cake") == "Positive"
    assert app.vader_analyse("There is a cat") == "Neutral"
    assert app.vader_analyse("I hate this project") == "Negative"

def test_accuracy():
    assert app.get_accuracy() >= 0.8