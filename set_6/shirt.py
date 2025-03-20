import os
from PIL import Image
from PIL import ImageOps
import sys


def main():
    check_length(sys.argv)
    ext(sys.argv[1], sys.argv[2])
    try:
        crop(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


# make sure user enters 2 command-line arguments
def check_length(x):
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return


# check ext types are allowed and the same for both inputs
def ext(a, b):
    l = [".jpg", ".jpeg", ".png"]
    # check argv1
    f, exta = os.path.splitext(a)
    g, extb = os.path.splitext(b)
    if exta not in l or extb not in l:
        sys.exit("Invalid input")
    elif exta != extb:
        sys.exit("Input and output have different extensions")
    else:
        pass


def crop(a, b):
    # create objects for input and pasting images
    Input_Image = Image.open(a)
    shirt = Image.open("shirt.png")

    # resize input based on size of pasting image
    New_Input = ImageOps.fit(Input_Image, shirt.size)

    # paste shirt onto inpu
    New_Input.paste(shirt, (0, 0), shirt)
    final = New_Input

    name, ext = os.path.splitext(b)

    # save correct file type
    print(name, ext)
    if ext in [".jpg", ".jpeg"]:
        b = name + ".jpg"
    else:
        b = name + ".png"
    # save image as output
    final.save(b)


if __name__ == "__main__":
    main()
