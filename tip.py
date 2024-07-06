def main():
    dollars = (input(("How much was the meal? ").strip))
    percent = float((input("What percentage would you like to tip? ").rstrip("%")))/100
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()
