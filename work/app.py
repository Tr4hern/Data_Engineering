import redis
import vader
from flask import Flask, request, jsonify

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
    return jsonify("{}".format(vader.vader_analyse(request.args.get("message"))))

