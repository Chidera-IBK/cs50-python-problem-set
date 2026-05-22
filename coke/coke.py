print("Amount Due: 50")

account = 0

while True:
    payed = int(input("Insert Coin: "))
    if payed == 25 or payed == 10 or payed == 5:
        account += payed
        if account < 50:
            print("Amount Due:", 50 - account)
        elif account >= 50:
            print("Change Owed:", account - 50 )
            break
    else:
        print("Amount Due: 50")
        continue
