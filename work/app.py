import redis
import toxicity
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/sentiment', methods=['GET'])
def sentiment():
    print("fetch")
    result = toxicity.detoxify_json_to_string(toxicity.detoxify_analyse(request.args.get("message")))
    print(result)
    return jsonify("{}".format(result))

