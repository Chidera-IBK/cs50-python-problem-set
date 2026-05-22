import requests


artist = input("Enter An Artist Name: ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + artist)
response = response.json()

for song in response["results"]:
    print(f"* {song['trackName']}")
