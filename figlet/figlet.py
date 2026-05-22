import pyfiglet
import sys


args = sys.argv


if len(args) == 1:
    text = input("Input: ")
    figlet = pyfiglet.figlet_format(text)
    print("Output:\n", figlet)
else:
    font_name = args[2]
    if len(args) >= 3 and args[1] in ("-f", "--font") and font_name in pyfiglet.FigletFont.getFonts():
        text = input("Input: ")
        figlet = pyfiglet.figlet_format(text, font=font_name)
        print("Output:\n", figlet)

    else:
        sys.exit("Usage: script.py [-f FONTNAME]")
