# Refer to this module's readme

from museum.artwork import get_artwork
from museum.artists import get_artists

def main():
    artist = input("Artist: ")
    artworks = get_artists(query=artist, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

main()