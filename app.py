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
    # n = 15  # 나중에 index에서 숫자 변수 받아올 자리
    results = spotify.search(q='snow',
                             type='track', limit=5)
    return results
    # 내가 필요한 정보들 list로 만들어서 html로 보내기 -- 일단은 한개만
    result = results[0]
    # for result in results:
    track_title = result['tracks']['items']['name']
    album_name = result['tracks']['items']['album']['name']
    album_image = result['tracks']['items']['album']['images'][0]['url']
    artist_name = result['tracks']['items']['artists']['name']
    preview_url = result['tracks']['items']['preview_url']

    track_info = {'title': track_title, 'artist': artist_name, 'album': album_name,
                  'album image': album_image, 'preview': preview_url}

    return jsonify({'result': 'success', 'tracks': track_info})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
