import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)


@app.route('/')
def main():
    return "Test webapp"