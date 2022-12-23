import json
import requests
import sys

# exit progam if user doesn't enter a band
if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# print track name
o = response.json()
for result in o["results"]:
    print(result["trackName"])
