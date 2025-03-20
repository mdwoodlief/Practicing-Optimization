def main():
    Total = 0.00
    while True:
        try:
            new_item = get_price()
            Total += new_item
            print(f"Total: ${Total:.2f}")
        except KeyError:
            print("Invalid menu item.")
        except EOFError:
            break


def get_price():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    x = input("Item: ").title()
    return menu[x]


main()
