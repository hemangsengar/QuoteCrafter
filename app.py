from flask import Flask, render_template,request
from Quotes import *

app = Flask(__name__)


@app.route('/')
def home():
    title = "AI Quotes"
    return render_template("index.html",title=title)


@app.route('/result', methods=['POST'])
def about():
    input = request.form.get("Insipration")
    Responce = getQuotes(input)
    print(Responce)
    title = "Quote"
    return render_template("result.html",title =title, Responce=Responce)
#if __name__ == "__main__":
    