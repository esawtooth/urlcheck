#!/usr/bin/env python

import whois
import flask
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True
# app.config['SERVER_NAME'] = "aws.rohitja.in"

@app.route("/geturl", methods = ["POST"])
def getUrl():
    urlRequested = flask.request.form['url']
    info = getUrlAvailability(urlRequested)
    if info:
        print urlRequested, info
        return "The requested url is not available. It will expire on " + str(info)
    else:
        return "Contratulations: The requested url is available."

@app.route("/")
def front():
    return flask.render_template("./index.html")

def getUrlAvailability(url):
    w = whois.whois(url)
    return w.expiration_date

if __name__ == "__main__":
    app.run(host="0.0.0.0")
