import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level < 1:
        continue
    else:
        break

ran = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess < 1:
        continue
    elif guess < ran:
        print("Too small!")
    elif guess > ran:
        print("Too large!")
    else:
        print("Just right!")
        break



