import sys

def main():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    file = sys.argv[1]
    if not file.endswith(".py"):
        print("Not a python file")
        sys.exit(1)

    try:
        lines = count_lines(file)
        print(lines)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


def count_lines(filename):
    code_lines = 0

    with open(filename, "r") as f:
        for line in f:
            stripped = line.strip()

            if  stripped == "" or stripped.startswith("#"):
                continue

            code_lines += 1

    return code_lines


if __name__ == "__main__":
    main()

