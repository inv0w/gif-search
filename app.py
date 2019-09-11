from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # Set parameters
    apikey = '3KIVL54QFKNV'
    lmt = 10
    search_term = request.args.get("search")

    # Make dict from parameters
    params = {'q': search_term, 'key': apikey, 'limit': lmt}

    # Call API and load first ten results
    r = requests.get("https://api.tenor.com/v1/search", params=params)
    first_ten = json.loads(r.content)["results"]

    # Render the 'index.html' template
    return render_template("index.html", first_ten=first_ten)


if __name__ == '__main__':
    app.run(debug=True)
