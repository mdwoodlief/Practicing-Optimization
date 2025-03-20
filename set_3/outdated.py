def main():
    # Define list of months
    ML = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    # Get entry
    u = input("Date: ")

    while True:
        if "/" not in u:
            try:
                month, r = u.split(" ", 1)
                day, year = r.split(",", 1)
            except ValueError:  # catch less than 2 itemns to split on lines 12 + 13
                u = input("Date: ").lstrip()
            else:
                try:
                    m = ML.index(month) + 1
                except ValueError:  # Catch value error on m not a month
                    u = input("Date: ").lstrip()
                    continue
                else:
                    d = int(day)
                    if 31 >= d >= 1 and 12 >= m >= 1:
                        y = int(year)
                        # Use f string to format with leading 0s
                        print(f"{y}-{m:02}-{d:02}")
                        break
                    else:
                        u = input("Date: ").lstrip()

        else:
            month, day, year = u.split("/", 2)
            try:
                m = int(month)
                d = int(day)
                y = int(year)
                if 31 >= d and d >= 1 and 12 >= m and m >= 1:
                    print(f"{y}-{m:02}-{d:02}")
                    break
                else:
                    u = input("Date: ").lstrip()
            except ValueError:  # Catch str that can't be converted to int
                u = input("Date: ").lstrip()


main()
