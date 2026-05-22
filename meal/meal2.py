def main():
    clock = input("What time is it? ")
    time = convert(clock)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

    else:
        print("", end = "")


def convert(time):
    t = float(time.replace(":", "."))
    return t

if __name__ == "__main__":
    main()
