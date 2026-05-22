import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    doc = sys.argv[1]
    if not doc.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    with open(doc) as file:
        reader = csv.DictReader(file)

        try:
            tab_ver = tabulate(reader,headers={},tablefmt="grid")
            print(tab_ver)
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
main()
