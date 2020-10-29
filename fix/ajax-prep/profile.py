import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    return render_template("index.html")



@app.route('/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.form['name']
    # TODO: get the values from the rest of the form
    # Add them to jsonify
    
    return jsonify({'fullname': fullname, })





if __name__ == "__main__":
    app.run(debug=True)