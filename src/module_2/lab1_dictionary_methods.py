# Refer to this module's readme

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Here are yesterday's answers:")

    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")

main()