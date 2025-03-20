import random
import sys

while True:
    Level = input("Level: ".lstrip())
    try:
        Level = int(Level)
    except ValueError:
        None
    else:
        if Level > 0:
            break
        else:
            None
L = list(range(1, Level + 1))
C = random.choice(L)

while True:
    Guess = input("Guess: ".lstrip())
    try:
        Guess = int(Guess)
    except ValueError:
        None
    else:
        if Guess > C:
            print("Too large!")
        elif Guess < C:
            print("Too small!")
        else:
            print("Just right!")
            break
sys.exit
