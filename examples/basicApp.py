#!/usr/bin/env python

from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def home(): 
    return  render_template("index.html")


@app.route('/Record/')
def record(): 
    return  render_template("audio-video.html")

@app.route('/Contact/')
def contact(): 
    return  render_template("formpage.html")



@app.route('/bacon', methods=['GET', 'POST'])
def bacon(): 
    if request.method == 'POST':
        return "Using POST"
    else: 
        return "Probably using GET"






if __name__ == "__main__":
    app.run(debug=True)
