import random
import sys


def main():
    level = get_level()
    i = 10  # counter for questions
    c = 3  # counter for guesses
    score = 0
    while i > 0:  # loop for 10 questions
        a = generate_integer(level)
        b = generate_integer(level)
        c = 3  # counter for guesses
        while c >= 0:  # loop for 3 guesses per question
            try:
                ans = int(input((f"{str(a)} + {str(b)} = ").lstrip()))
            except ValueError:
                c -= 1
                if c == 0:
                    print((f"{str(a)} + {str(b)} = {a+b} "))
                    break
                else:
                    print("EEE")
            else:
                if ans == a + b:  # next question
                    score += 1
                    break
                else:
                    c -= 1
                    if c == 0:
                        print((f"{str(a)} + {str(b)} = {a+b}"))
                        break
                    else:
                        print("EEE")

        i -= 1
    print(f"Score: {score}")
    sys.exit


def get_level():
    e = ["1", "2", "3"]
    while True:
        n = input("Level: ").lstrip()
        try:  # catch values outside n 1-3
            if n in e:
                return n
        except ValueError:
            pass


def generate_integer(level):
    try:
        x = int(level)
    except ValueError:
        pass
    else:
        # define randrange start and stops
        if x == 1:
            k = 0
            h = 9
        elif x == 2:
            k = 10
            h = 99
        else:
            k = 100
            h = 999
        return random.randint(k, h)


if __name__ == "__main__":
    main()
