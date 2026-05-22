words = {"PAN": 4, "CAN": 4, "RAN": 5}

def main():
    print("Welcome to the spelling bee game!!")
    print("Make a word from the following letters p, a ,r ,n, c")



    while True:
        guess = input("Spell a word: ")
        if guess in words.keys():
            print(f"Correct you have successfully gotten {words[guess]} points")
            words.pop(guess)
            print(f"You can still make {len(words)} more words from the given letters")
            print("Try again")

        else:
            print("You didn't form a correct word you have lost")
            break


main()
