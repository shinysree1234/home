from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return"hello"
@app.route("/home")
def home():
    return"welcome to my home page"
@app.route("/about")
def about():
    return"welcome to home"
if(__name__=="__main__"):
    app.run(debug="true")