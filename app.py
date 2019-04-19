#!/usr/bin/env python

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/record')
def record():
    return render_template("record.html")


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "Using POST"
    else:
        return "Probably using GET"


if __name__ == "__main__":
    app.run(debug=True)
