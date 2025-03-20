def main():
    print(value(input("Input a greeting: ")))


def value(greeting):
    g = greeting.casefold().strip()
    if g.find("hello") >= 0:
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
