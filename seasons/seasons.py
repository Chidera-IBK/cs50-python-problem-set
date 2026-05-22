from datetime import date
import re
import inflect
import sys

p = inflect.engine()
def main():
    print(edited(input("Date of Birth: ")))

def edited(dob):
    if expected := re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", dob):
        year = int(expected.group(1))
        month = int(expected.group(2))
        day = int(expected.group(3))

        days = date.today() - date(year, month, day)
        minutes = 24*60*days.days

        words = p.number_to_words(minutes)
        output = words.replace(" and ", " ") + " minutes"
        return output.capitalize()
    else:
        return sys.exit("Invalid date")


if __name__ == "__main__":
    main()
