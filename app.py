from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    title = "Hemang's Portfolio"
    return render_template("index.html",title=title)

@app.route('/about')
def about():
    title = "About"
    names = ["Hemang", "Maya", "Sally"]
    return render_template("about.html",names=names)
#if __name__ == "__main__":
    