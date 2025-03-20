# import for command-line arguments
import sys
import csv


def main():
    # check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Use 3 command-line arguments")
    try:
        # function to read current file
        examine(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        pass
    # create improved file
    # create(x)


def examine(x, b):
    # open file to read
    with open(x, "r", newline="") as f:
        reader = csv.DictReader(f)

        # open file to write to
        with open(b, "w", newline="") as F:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(F, fieldnames=fieldnames)
            writer.writeheader()

            # split values from DictReader [name] into first and last
            for row in reader:
                full = row["name"]
                house = row["house"]
                last, first = [x.strip() for x in full.split(",")]
                # write to new file, inside loop
                writer.writerow({"first": first, "last": last, "house": house})


if __name__ == "__main__":
    main()
