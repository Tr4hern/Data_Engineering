import vader


def test_sentiment():
    assert vader.vader_analyse("I love cake") == "Positive"
    assert vader.vader_analyse("There is a cat") == "Neutral"
    assert vader.vader_analyse("I hate this dog") == "Negative"

def test_accuracy():
    assert vader.get_accuracy(2000) >= 0.6, "vader accuracy is < 0.6"
    # because we run the the tests in the Dockerfile, we can't allow us to have a failure, so we check the accuracy is above 60% (generally around 70% for this dataset)