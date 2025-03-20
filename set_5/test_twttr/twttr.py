def main():
    word = input("User input: ").strip()
    print(shorten(word))


def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    C = ""
    for char in word:
        if char in vowels:
            continue
        else:
            C += char
    return C


if __name__ == "__main__":
    main()
