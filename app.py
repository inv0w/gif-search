from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # Set parameters
    apikey = '3KIVL54QFKNV'
    lmt = 9
    search_term = request.args.get("search")

    # Make dict from parameters
    params = {
        'q': search_term,
        'key': apikey,
        'limit': lmt
        }

    # Call API and load first ten results
    r = requests.get("https://api.tenor.com/v1/search", params=params)
    if r.status_code == 200:  # If the request was successful
        first_gifs = json.loads(r.content)["results"]
    else:
        first_gifs = None

    # Render the 'index.html' template
    return render_template("index.html", first_gifs=first_gifs)


@app.route('/trending')
def trending():
    """Return trending gifs"""
    apikey = '3KIVL54QFKNV'
    lmt = 9

    # Make dict of parameters
    params = {
        'key': apikey,
        'limit': lmt
    }

    r = requests.get("https://api.tenor.com/v1/trending", params=params)
    if r.status_code == 200:  # If the request was successful
        first_gifs = json.loads(r.content)["results"]
    else:
        first_gifs = None

    return render_template("index.html", first_gifs=first_gifs)


if __name__ == '__main__':
    app.run(debug=True)
