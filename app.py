import redis
from flask import Flask
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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
def index():
    return  '''
                <label for="text">Text Input:</label><br>
                <input type="text" id="text" name="text" value=""><br>
                <button type="button" onclick="getInfo()"> Analyse </button><br>
                <p id = "result"></p><br>

                <script>
                function getInfo() {
                    document.getElementById("result").innerHTML = vader_analyse(document.getElementById("text").value);
                }
                </script>'''