import os
import json
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    active_page = 'about'
    return render_template("index.html", active_page=active_page)


@app.route("/pt")
def pt():
    active_page = 'trainer'
    return render_template("pt.html", page_title="Personal Trainer",
                           active_page=active_page)


@app.route("/member")
def member():
    active_page = 'member'
    return render_template("member.html", page_title="Members",
                           active_page=active_page)


@app.route("/pt/book")
def book():
    active_page = 'book'
    return render_template("book.html", page_title="Book",
                           active_page=active_page)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
