import sys


def main():
    # checking for proper number of command line arguments
    if len(sys.argv) != 2:
        sys.exit("Use two command-line arguments")
    else:
        name, ext = sys.argv[1].rsplit(
            ".",
        )
        if ext != "py":
            sys.exit("Not a Python file")

    # trying to open .py file
    try:
        print(len(line_counter(sys.argv[1])))
    except FileNotFoundError:
        print("File does not exist")


def line_counter(x):
    with open(x, "r") as file:
        lines = file.readlines()
        # list to return for counting
        count_list = []
        for line in lines:
            if line.lstrip().startswith(
                "#"
            ):  # remove lines that are ONLY comments, not containing comments
                continue
            elif line.strip() == "" or line == "\n":
                continue
            else:
                count_list.append(line)
        return count_list


if __name__ == "__main__":
    main()
