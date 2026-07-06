amount_due = 50

while True:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert coin: "))

    if coin in [5, 10, 25]:
        amount_due -= coin

    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
        break
