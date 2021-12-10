import redis
import pandas as pd
from flask import Flask, request, jsonify
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

    df = pd.read_csv('Reddit_Data.csv')

    for i in range(0, len(df)):
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


@app.route('/')
def index():
    return  '''
                <label for="text">Text Input:</label><br>
                <input type="text" id="text" name="text" value=""><br>
                <button type="button" onclick="getInfo()"> Analyse </button><br>
                <p id = "result"></p><br>

                <script>
                function getInfo() {
                    var message = document.getElementById("text").value
                    var analyzing = fetch('http://localhost:5000/sentiment?message='+message)
                    .then((analyzing) => analyzing.json())
                    .then((json) => {
                        document.getElementById("result").innerHTML = json
                        console.log(json)
                    })
                }
                </script>'''

@app.route('/sentiment', methods=['GET'])
def sentiment():
    return jsonify("{}".format(vader_analyse(request.args.get("message"))))

