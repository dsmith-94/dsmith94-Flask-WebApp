# module 10 - Flask Application
# Mike Colbert 10/28/2025

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/Daw")
def Daw():
    x = 6
    y = 15
    z = x + y
    name = "Daw"
    return f"{name}, the sum of {x} and {y} is {z}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
