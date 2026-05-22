def main():
    text = input("Input: ")

    twttr_form = shorten(text)

    print("Output:", twttr_form)

def shorten(word):
    new_text = ""
    for char in word:
        if char not in ['a','e','i','o','u','A','E','I','O','U']:
            new_text += char
    return new_text

if __name__ == "__main__":
    main()
