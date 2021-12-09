import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host = 'redis', port = 6379)


@app.route('/')
def index():
    label = '<label for="text">Text Input:</label>'
    text = '<input type="text" id="text" name="text" value="">'
    button = "<button type=\"button\"> Button </button>"
    br = '<br>'

    return '<form action="/action_page.php">' + label + br + text + br + button +'</form>'
    #return '<form action="/action_page.php"><label for="text">Text Input:</label><br><input type="text" id="text" name="text" value=""><br><br><button onclick="doSomething()" type="button"> Button </button><p id="test">Hello</p><script>function doSomething(){document.getElementById("test).innerHTML = "Good Bye ";</script>}</form>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')