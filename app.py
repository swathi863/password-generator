from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    password = ""

    if request.method == "POST":

        length = int(request.form["length"])

        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*()"

        all_characters = letters + numbers + symbols

        for i in range(length):
            password += random.choice(all_characters)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)