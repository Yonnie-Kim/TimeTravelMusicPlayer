import spotipy
import requests
import urllib
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

cid = 'a618b89079584773b973a20f6009a5bd'
secret = '7cccffcaf51f44ecbafb3d59a367adce'
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret)

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tracks', methods=['POST'])
def search_tracks():
    past_year = request.form['past_year']
    keyword = request.form['keyword']
    query = keyword + ' year:' + str(past_year)
    results = spotify.search(q=query, type='track', limit=5)
    return results
    return jsonify({'result': 'success', 'tracks': results})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
