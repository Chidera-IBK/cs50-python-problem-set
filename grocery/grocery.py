import sys
items = []

while True:

    try:
        item = input("")
        items.append(item)

    except EOFError:
        for i in sorted(set(items)):
            print(f"{items.count(i)} {i.upper()}")
        sys.exit()
