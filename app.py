import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)

@app.route('/')
def index():
    return  '''
                <label for="text">Text Input:</label><br>
                <input type="text" id="text" name="text" value=""><br>
                <button type="button" onclick="getInfo()"> Analyse </button><br>
                <p id = "result"></p><br>

                <script>
                function getInfo() {
                    document.getElementById("result").innerHTML = document.getElementById("text").value;
                }
                </script>'''