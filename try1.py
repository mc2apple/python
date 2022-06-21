
import random

def main():
    """Start a Periodic table."""
    print("Guess the Alkali metals!")

    Alkali = [
        "Lithium",
        "Sodium",
        "Potassium",
        "Rubidium",
        "Caesium",
        "Francium",
        ]

    x = random.choice(Alkali)
    guess = None

    while x != guess:

        guess = str(input("What Alkali am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()