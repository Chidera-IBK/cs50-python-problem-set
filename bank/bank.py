def main():
    responds = input("Greeting: ").lower().strip()
    print(f"${value(responds)}")

def value(responds):
    if responds.startswith("hello"):
        return 0
    elif responds.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
