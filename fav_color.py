def main():
    #Ask user for color and provide temp and complementary color
    fav=input("Consider 'red', 'green', 'yellow', blue', 'purple', and 'orange;."
              "Which is your favorite color? ").casefold().strip()
    #list to validate input
    valid = ["red", "organge", "yellow", "blue", "green", "purple"]
    if fav in valid:
        temp(fav)
        comp(fav)
    else:
        print("Enter a valid color.")


def temp(x):
    #list for warm colors
    warm = ["red", "organge", "yellow"]
    if x in warm:
        print(f"{x.capitalize()} is a \"warm\" color.", end=" ")
    else:
        print(f"{x.capitalize()} is a \"cool\" color.", end=" ")
        


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
 
    print(x.capitalize(), "is the complementary color of " + comp_colors[x] +".")
  

main()
