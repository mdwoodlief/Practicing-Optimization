def main():
    Time = input("What time is it? ").strip()
    Total = convert(Time)

    if Total >= 7.0 and Total <=8.0:
        print("breakfast time")

    elif Total >= 12.0 and Total <=13.0:
        print("lunch time")

    elif Total >= 18.0 and Total <=19.0:
        print("dinner time")


def convert(x):
    a, b = x.split(":", maxsplit=1)
    Hour = int(a)
    Minute = int(b)/60
    Total = Hour+Minute
    return Total

if __name__ == "__main__":
    main()