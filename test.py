import sys

def main():
    if len(sys.argv) < 1:
        print ("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    try:
        file = sys.argv[1]
        count(file)
    except IndexError:
        print("Too few command-line arguments")
    except FileNotFoundError:
        print("File does not exist")

def count(file):
    with open(file, "r") as f:
        count = 0
        for line in f:
            if "#"  in line or line.strip() == "":
                continue
            count += 1
        print (count)


if __name__ == "__main__":
    main()


