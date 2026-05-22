import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    text = s.split(" ")

    for word in text:
        if re.search(r"\bum\b", word, re.IGNORECASE):
            counter += 1
    return counter

...


if __name__ == "__main__":
    main()
