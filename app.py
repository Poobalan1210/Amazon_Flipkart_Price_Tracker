import webbrowser
import requests
from flask import Flask, render_template, request, url_for, redirect
import pyrebase

config = {
    "apiKey": "AIzaSyC5PuJj7QcRNIjIeI32EczKTaVa6mhuVyg",
    "authDomain": "flipkart-price-tracker.firebaseapp.com",
    "databaseURL": "https://flipkart-price-tracker-default-rtdb.firebaseio.com",
    "projectId": "flipkart-price-tracker",
    "storageBucket": "flipkart-price-tracker.appspot.com",
    "messagingSenderId": "1044509919052",
    "appId": "1:1044509919052:web:bf45df6c22986e8f1031e9",
    "measurementId": "G-RESS01LCH6"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

app = Flask(__name__)


def add_database(amazon_url, flipkart_url, budget_price, mailid):
    data = {}
    data["amazon_url"] = amazon_url
    data["flipkart_url"] = flipkart_url
    data["budget_price"] = budget_price
    data["mailid"] = mailid
    db.child("Users").child(mailid.strip(".com")).set(data)


@app.route("/", methods=["POST", "GET"])
def getval():

    if request.method == "POST":
        amazon_url = request.form["amazon_url"]
        flipkart_url = request.form["flipkart_url"]
        budget_price = request.form["budget_price"]
        mailid = request.form["email_id"]
        add_database(amazon_url, flipkart_url, budget_price, mailid)
        return render_template("main.html")

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
