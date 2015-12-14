#!/usr/bin/env python

import whois
import flask
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True
fileName = "urllist"
# app.config['SERVER_NAME'] = "aws.rohitja.in"

@app.route("/geturl", methods = ["POST"])
def getUrl():
    url = flask.request.form['url']
    email = flask.request.form['email']
    info = getUrlAvailability(url)
    if info:
        logRequest(url, email, info)
        print url, email, info
        return "The requested url is not available. It will expire on " + str(info) + ". We will email you when it is available."
    else:
        return "Contratulations: The requested url is available."

@app.route("/")
def front():
    return flask.render_template("./index.html")

def getUrlAvailability(url):
    w = whois.whois(url)
    return w.expiration_date
def logRequest(url, email, info):
    with open(fileName, 'a') as f:
        f.write(str(url) + "|" + str(email) + str(info) + "\n" + "----------" + "\n")
if __name__ == "__main__":
    app.run(host="0.0.0.0")
