def main():
    print(
        gauge(convert(input("What is the fuel gauge reading in a fraction? ").strip()))
    )


def convert(x):
    n, d = x.split("/")
    while True:

        try:
            N = int(n)
            D = int(d)
            R = round(N / D * 100)
        except ValueError:
            raise ValueError("Enter an appropriate value.")
        except ZeroDivisionError:
            raise ZeroDivisionError("Divisor cannot be zero.")
        if n > d and d != 0:
            raise ValueError("Numerator greather than denominator")
        else:
            return R


def gauge(i):
    if i >= 99:
        return "F"
    elif i <= 1:
        return "E"
    else:
        return f"{i}%"


if __name__ == "__main__":
    main()
