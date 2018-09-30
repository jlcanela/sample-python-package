from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/post', methods=['GET', 'POST'])
def post():
    return "post content"

