# Refer to this module's readme

import random

cards = ["jack", "queen", "king"]

def main():
    random.seed(0)
    print(random.sample(cards, k=2))

main()