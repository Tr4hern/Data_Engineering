import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)

def vader_analyse(text):
    analyser = SentimentIntensityAnalyzer()
    prediction = analyser.polarity_scores(text)
    score = prediction['compound']

    if score >= 0.05:
        return "Positive"
    if score <= -0.05:
        return "Negative"
    return "Neutral"


def get_accuracy():

    good_ones = 0
    cpt = 0

    with open('dataset.txt') as file:
        for line in file.readlines():
            score, text = line.strip().split('\t')

            score = float(score)
            if score >= 0.05:
                sentiment =  "Positive"
            else :
                if score <= -0.05:
                    sentiment =  "Negative"
                else:
                    sentiment =  "Neutral"

            predicted_sentiment = vader_analyse(text)

            good_ones += 1
            if sentiment == predicted_sentiment:
                cpt += 1

    return (good_ones / cpt)


@app.route('/')
def main():
    return "Test webapp"