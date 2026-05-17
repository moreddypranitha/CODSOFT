import sys
import os

# Add parent folder to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request
from responses import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        user_input = request.form["message"]

        response = get_response(user_input.lower())

    return render_template("index.html", response=response)

if __name__ == "__main__":

    app.run(debug=True)