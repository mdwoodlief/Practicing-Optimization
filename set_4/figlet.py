import sys, random
from pyfiglet import Figlet

figlet = Figlet()
L = figlet.getFonts()

if len(sys.argv) == 3:  # specific font choice
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    else:
        if sys.argv[2] not in L:  # catch invalid font
            sys.exit("Invalid usage")
        else:
            e = input("Input: ".lstrip())
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(e))

elif len(sys.argv) == 1:  # random font choice
    e = input("Input: ".lstrip())
    figlet.setFont(font=random.choice(L))
    print(figlet.renderText(e))


else:  # invalid entry
    sys.exit("Invalid usage")
