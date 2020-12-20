import pprint
import spotipy
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


@app.route('/tracks')
def search_tracks():
    # n = 15  # 나중에 index에서 숫자 변수(n년전) 받아올 자리
    # 쿼리조건 뭐 넣을지..수정필요!!
    results = spotify.search(q='Christmas',
                             type='track', limit=5)
    return results
    return jsonify({'result': 'success', 'tracks': results})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
