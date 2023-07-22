from flask import Flask,redirect,url_for

app=Flask(__name__)


@app.route('/') #decorator to define the route for our application
def home():
    return "Welcome Home"



if __name__=="__main__":
    app.run()