#!/usr/bin/env python

import random

def main():
    """Start a guessing game."""
    print("Guess the noble gas in the periodic table!")

    noblegas = [
        "He -Helium",
        "Ne -Neon",
        "Ar -Argon ",
        "Kr -Kryton",
        "Xe -Xenon",
        "Rn -Redon",
        "Og -Oganesson"
        ]

    x = random.choice(noblegas)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What noble gas am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))


main()