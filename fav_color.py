def main():
    #Ask user for color and provide temp and complementary color
    fav=input("Consider 'red', 'green', 'yellow', blue', 'purple', and 'orange;."
              "Which is your favorite color? ").casefold().strip()
    temp(fav)
    comp(fav)


def temp(x):
    #create 2 lists to search for input
    warm = ["red", "organge", "yellow"]
    cold = ["blue", "green", "purple"]
    if x in warm:
        print(f"{x.capitalize()} is a \"warm\" color.", end=" ")
    elif x in cold:
        print(f"{x.capitalize()} is a \"cool\" color.", end=" ")
    else:
        print("Enter a valid color.")


def comp(x):
    #create dict with complementary colors red/green, purple/yellow, orange/blue
    comp_colors = {
        "red":"green",
        "purple":"yellow",
        "orange":"blue",
        "green":"red",
        "yellow":"purple",
        "blue":"orange"
        }
    #Create a list for checking valid entry
    color_list = ["red", "organge", "yellow", "blue", "green", "purple"]
    if x in color_list:
        print(x.capitalize(), "is the complementary color of " + comp_colors[x] +".")
    else:
        None
main()