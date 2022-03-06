from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi_mundo():
    return "<p>Hi mundo!</p>"
