from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    password = ""
    error = ""

    if request.method == "POST":

        length = int(request.form["length"])

        characters = ""

        if "lowercase" in request.form:
            characters += string.ascii_lowercase

        if "uppercase" in request.form:
            characters += string.ascii_uppercase

        if "numbers" in request.form:
            characters += string.digits

        if "symbols" in request.form:
            characters += string.punctuation

        if characters == "":
            error = "Please select at least one option!"

        else:
            password = ''.join(
                secrets.choice(characters)
                for _ in range(length)
            )

    return render_template(
        "index.html",
        password=password,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)