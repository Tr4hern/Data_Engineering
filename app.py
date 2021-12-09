import redis
import pandas as pd
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

    df = pd.read_csv('Reddit_Data.csv')

    for i in range(0, len(df)):
        text = df["clean_comment"][i]
        score = df["category"][0]

        # Return the sentiment based on the column "category"
        if score == 1:
            sentiment =  "Positive"
        else :
            if score == -1:
                sentiment =  "Negative"
            else:
                sentiment =  "Neutral"
    
        # Return the sentiment based on the column "clean_comment"
        predicted_sentiment = vader_analyse(text)

        # calculate the accuracy
        good_ones += 1
        if sentiment == predicted_sentiment:
            cpt += 1

    return (good_ones / cpt)


@app.route('/')
def main():
    return "Test webapp"