import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

file1 = sys.argv[1].lower()
file2 = sys.argv[2].lower()

fn1, fext1 = file1.split(".")
fn2, fext2 = file2.split(".")

if not file1.endswith((".png",".jpeg")) and file2.endswith(("png",".jpeg")):
    sys.exit("Invalid input")
if not fext1 == fext2:
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")
try:
    image = Image.open(file1)
except FileNotFoundError:
    sys.exit("Input does not exist")
image = ImageOps.fit(image, shirt.size)
image.paste(shirt, shirt)
image.save(file2)
