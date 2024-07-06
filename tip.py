def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


    # change $xx.xx to xx.x
    #use str.lstrip([char]) to remove $
    #Convert to int before float?
def dollars_to_float(d):
    dollars=float((d).lstrip("$"))
    return dollars


# change xx% to 0.xx
def percent_to_float(p):
    perc=float((p).rstrip("%"))/100
    return perc


main()
