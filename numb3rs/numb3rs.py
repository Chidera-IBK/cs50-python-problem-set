import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    numbers = ip.split(".")

    if len(numbers) != 4:
        return False
    for number in numbers:
        if int(number) > 255:
            return False
        if number.startswith("0") and len(number) > 1:
            return False
    return True


if __name__ == "__main__":
    main()
