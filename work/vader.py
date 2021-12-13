import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def vader_analyse(text):
    analyser = SentimentIntensityAnalyzer()
    prediction = analyser.polarity_scores(text)
    score = prediction['compound']

    if score >= 0.05:
        return "Positive"
    if score <= -0.05:
        return "Negative"
    return "Neutral"



def get_accuracy(length):

    
    good_ones = 0
    cpt = 0

    df = pd.read_csv('Reddit_Data.csv')

    if(length <= 0):
        length = 1
    if(length > len(df)):
        length = len(df)

    for i in range(0, length):
        text = str(df["clean_comment"][i])
        score = int(df["category"][i])

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
        cpt += 1
        if sentiment == predicted_sentiment:
            good_ones += 1

    return (good_ones / cpt)