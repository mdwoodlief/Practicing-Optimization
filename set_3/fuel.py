"""
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.

"""


def main():

    while True:
        try:
            F = 2
            G = 1
            while F > G and G != 0:
                n, d = get_fuel().split("/")
                F = N = int(n)
                G = D = int(d)
            convert(N, D)
        except ValueError:
            print("Enter an appropriate value.")
        except ZeroDivisionError:
            print("Divisor cannot be zero.")
        else:
            break


def get_fuel():
    x = input("What is the fuel gauge reading in a fraction? ").strip()
    return x


def convert(N, D):
    perc = round(N / D * 100)
    if perc >= 99:
        print("F")
    elif perc <= 1:
        print("E")
    else:
        print(f"{perc}%")


main()
