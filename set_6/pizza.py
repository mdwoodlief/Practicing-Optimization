import sys  # necessary for command-line arguments
from tabulate import tabulate  # necessary for ASCII output


# CSV module is part of standard library, no need to import
def main():
    check_len(sys.argv)
    check_type(sys.argv[1])
    print(tabulate(read(sys.argv[1]), headers="firstrow", tablefmt="grid"))


def check_len(x):
    if len(x) != 2:
        sys.exit("Requires 1 command-line argument")
    else:
        pass


def check_type(x):
    name, ext = x.rsplit(".")
    if ext != "csv":
        sys.exit("Not a CSV file")


def read(x):
    l = []
    try:
        # open file and tabulate
        with open(x, "r") as f:
            for line in f:
                pizza, small, large = line.rstrip().split(",")
                g = {"pizza": pizza, "small": small, "large": large}
                l.append(g)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return l


if __name__ == "__main__":
    main()
