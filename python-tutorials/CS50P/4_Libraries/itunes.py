import requests
import sys

# exit progam if user doesn't enter a band
if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response)
