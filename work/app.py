import redis
import toxicity
from flask import Flask, request, jsonify, render_template
from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram

start_http_server(8010)

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)

def beautitful_text(text):
    text = text.replace('\'', '')
    text = text.replace('\"', '')
    text = text.replace('{', '')
    text = text.replace('}', '')
    text = text.replace(',', '<br>')
    return text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sentiment', methods=['GET'])
def sentiment():
    result = toxicity.detoxify_json_to_string(toxicity.detoxify_analyse(request.args.get("message")))
    result = beautitful_text(result)
    return jsonify("{}".format(result))