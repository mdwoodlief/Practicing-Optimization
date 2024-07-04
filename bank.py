def main():
    Greeting=input("Input a greeting: ").lower().strip()
    if Greeting.find("hello") >=0:
        print("$0")
    elif Greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
