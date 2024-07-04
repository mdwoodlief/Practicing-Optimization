def main():
    equation = input("Enter your calculation: ").lstrip()
    split = equation.split(" ", maxsplit=2)
#split user entry into the 3 components
    x, y, z = split
#convert str entries to float
    a = float(x)
    b = float(z)

    if y == "+":
        print(a+b)
    elif y == "-":
        print (a-b)
    elif y == "*":
        print (a*b)
    else:
        print(a/b)

main()
