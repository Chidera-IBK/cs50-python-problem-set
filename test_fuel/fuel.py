def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))
    ...


def convert(fraction):
    x,y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError()
    if x > y:
        raise ValueError()
    if x < 0:
        raise ValueError()
    if y == 0:
        raise ZeroDivisionError()
    return round((x/y)*100)
    ...

def gauge(z):
    if z <= 1:
        return "E"
    elif z >= 99:
        return "F"
    else:
        return f"{z}%"


if __name__ == "__main__":
    main()
