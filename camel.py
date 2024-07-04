def main():
    CC = input("Enter a variable in camel case: ").strip()
    L= list(CC)
    for i in range(len(L)):
        if (L[i].isupper()):
            L[i] = "_"+L[i].casefold()
    print("".join(L))


main()
