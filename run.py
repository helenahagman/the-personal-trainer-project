import os
from flask import Flask, render_template 


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pt")
def pt():
    return render_template("pt.html")

@app.route("/member")
def member():
    return render_template("member.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)