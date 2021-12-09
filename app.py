import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)


@app.route('/')
def index():
    return '<form action="/action_page.php"><label for="text">Text Input:</label><br><input type="text" id="text" name="text" value=""><br><input type="submit" value="Submit"></form>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')