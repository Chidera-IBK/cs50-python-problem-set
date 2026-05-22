import random


def main():
    lvl_gotten = get_level()
    i = 0
    score = 0

    while i < 10:
        trial = 0
        i+=1
        x = generate_integer(lvl_gotten)
        y = generate_integer(lvl_gotten)
        ans = input(f"{x} + {y} = ")
        if  ans.isdigit() and (x + y) == int(ans) :
            score += 1
        else:
            print("EEE")
            for _ in range(2):
                trial += 1
                retry = input(f"{x} + {y} = ")
                if retry.isdigit() and int(retry) == (x+y):
                    score+=1
                    break
                else:
                    print("EEE")
                if trial == 2:
                    print(f"{x} + {y} = {x+y}")

    print("Score:", score)

def get_level():
    while True:
        level = input("Level: ")
        if level in ("1","2","3"):
            return int(level)
        else:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError("Invalid level: must be 1, 2, or 3")

    ...
if __name__ == "__main__":
    main()
