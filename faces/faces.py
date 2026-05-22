def main():
    text = input("")
    print(convert(text))

def convert(input):
    return input.replace(":)","🙂").replace(":(","🙁")

main()


