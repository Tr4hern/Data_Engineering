import pytest
import requests
import vader


def test_sentiment():
    assert vader.vader_analyse("I love cake") == "Positive"
    assert vader.vader_analyse("There is a cat") == "Neutral"
    assert vader.vader_analyse("I hate this project") == "Negative"

def test_accuracy():
    assert vader.get_accuracy(2000) >= 0.6, "vader accuracy is < 0.6"