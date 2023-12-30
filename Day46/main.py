from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get(url=f"{URL}{user_input}/")
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')
songs_list = [song.getText().strip() for song in soup.select("li ul li h3")]

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri="http://localhost/"))

list_of_uri = []
year = user_input.split("-")[0]
for song in songs_list:
    data = sp.search(q=f"track:{song} year:{year}", type="track")
    if data['tracks']['total'] == 0:
        continue
    list_of_uri.append(data['tracks']['items'][0]['uri'])


data = sp.current_user()
playlist_data = sp.user_playlist_create(user=data['id'], name=f"Bilboard {user_input}", public=False)
sp.playlist_add_items(playlist_id=playlist_data["id"], items=list_of_uri)


























# data = sp.search(q="Teenage Dream", type="track")
# print(data)
# print(data['tracks']['items'][0])
# pprint(data['tracks']['items'][0]['uri'])

# print(list_of_uri)
#
# test_song = sp.search(q="sjfgdspj", type="track")
# print(test_song)
# if test_song['tracks']['total'] == 0:
#     print("test")