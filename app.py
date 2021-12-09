import redis
from flask import Flask
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)

def vader_analyse(text):
    analyzeranalyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(text)
    return "{:-<40} {}".format(text, str(score))

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