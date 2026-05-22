names = []


try:
    while True:
        N = input("Name: ")
        names.append(N)
except EOFError:
    if len(names) == 1:
        print("\nAdieu, adieu, to", names[0])
    elif len(names) == 2:
        print("\nAdieu, adieu, to", names[0], "and", names[1])
    else:
        print("\nAdieu, adieu, to ", end="")
        for name in names[:-1]:
            print(f"{name}, ", end="")
        print(f"and {names[-1]} ")
