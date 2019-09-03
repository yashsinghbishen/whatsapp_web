from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    return render_template("web.html")


if __name__ == "__main__":
    app.run(debug=True)
