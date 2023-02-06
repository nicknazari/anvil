from flask import Flask

app = Flask('anvil')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/VerifyUser")
def verify_user():
    return "<p>Verified</p>"
