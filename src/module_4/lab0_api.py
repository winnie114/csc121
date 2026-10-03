# Refer to this module's readme

import sys
import requests

def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist, "limit": 3}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)
    
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")

main()