def main():
#get user str
    x = input("Enter a string of text: ")
    Vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
#create empty str variable to add to
    C = ""
#iterate over str input to select vowels to add to empty str
    for char in x:
        if char in Vowels:
            continue
        else:
            C += char
#print new str
    print(C)

main()
