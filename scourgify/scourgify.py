import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

file1 = sys.argv[1]
file2 = sys.argv[2]

try:
    with open(file1, newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = ["first", "last", "house"]

        with open(file2, "w") as f2:
            csv_write = csv.DictWriter(f2, fieldnames=fieldnames)
            csv_write.writeheader()
            for line in reader:
                first_name,last_name = line["name"].split(", ")
                csv_write.writerow({
                    "first": last_name,
                    "last": first_name,
                    "house": line["house"]
                })

except FileNotFoundError:
    sys.exit("Could not read "+ file1)


