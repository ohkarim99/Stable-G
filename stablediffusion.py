from flask import Flask,redirect,url_for

app=Flask(__name__)


@app.route('/') #decorator to define the route for our application
def home():
    return "Welcome Home"
@app.route("/<name>")
def g(name):
    return f"heloo {name}"


if __name__=="__main__":
    app.run()