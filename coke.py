def main():
#initial cost and acceptable coins
    cost = 50
    AccCoins = [25, 10, 5]
#Loop for payment
    while cost > 0:
        print(f"Amount Due: {cost}")
        payment = int(input("Insert Coin: ").casefold().strip())
        if payment in AccCoins:
            cost = cost - payment
#Loop for change. Could also write as bool
    while cost <= 0:
        print(f"Change Owed: {-1*cost}")
#break to exit infinite loop
        break

main()
