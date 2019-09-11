from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    apikey = '3KIVL54QFKNV'
    lmt = 10
    # TODO: Extract query term from url
    search_term = request.args.get("search")
    # TODO: Make 'params' dict with query term and API key
    params = {'search': search_term, 'apikey': apikey, 'limit': lmt}
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search", params = params)
    # TODO: Get the first 10 results from the search results
    first_ten = json.loads(r.content)["results"]
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("index.html", first_ten=first_ten)

@app.route('/search')
def search():
    search_input = request.args.get("search")
    apikey = '3KIVL54QFKNV'
    lmt = 10
    # TODO: Extract query term from url
    search_term = request.args.get("search")
    # TODO: Make 'params' dict with query term and API key
    params = {'search': search_term, 'apikey': apikey, 'limit': lmt}
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search", params = params)
    # TODO: Get the first 10 results from the search results
    first_ten = json.loads(r.content)["results"]
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("search.html", first_ten=first_ten)

if __name__ == '__main__':
    app.run(debug=True)
