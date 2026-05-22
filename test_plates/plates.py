def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.strip()
    #contains a maximum of 6 characters
    if len(s) > 6 or len(s) < 2:
        return False
    #starts with atleast two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    #check if numbers are used in the middle of the plate number
    numbers_started = False
    for char in s[2:]:
        if char.isdigit():
            numbers_started = True
        elif numbers_started and char.isalpha():
            return False
    #checks if the first number is zero
    check = []
    for char in s:
        if char.isdigit():
            check.append(char)

    if check and check[0] == "0":
        return False
    # checks if punctuation spaces and periods are include
    for char in s:
        if not all(char.isalnum() for char in s):
            return False
    return True

if __name__ == "__main__":
    main()
