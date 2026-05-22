import sys
items = []

while True:

    try:
        item = input("")
        items.append(item)

    except EOFError:
        print("\n")
        for i in set(items):
            print(f"{items.count(i)} {i.upper()}")
        sys.exit()








