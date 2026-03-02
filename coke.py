coke = 50
print(f"Amount Due: {coke}")

while coke > 0:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        coke -= coin
        if coke <= 0:
            print(f"Change Owed: {abs(coke)}")
        else:
            print(f"Amount Due: {coke}")
    else:
        print(f"Amount Due: {coke}")
