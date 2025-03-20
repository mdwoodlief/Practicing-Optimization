def main():
    answer=input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    if check(answer):
        print("Yes")
    else:
        print("No")


def check(x):
    return True if x == "42" or x == "forty-two" or x == "forty two" else False


main()
