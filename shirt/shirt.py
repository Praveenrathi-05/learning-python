import sys
import os
from PIL import Image,ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not(sys.argv[1].endswith(('.jpeg','.png','.jpg')) and sys.argv[2].endswith(('.jpeg','.png','jpg'))):
    sys.exit("Invalid input")
elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")

try:
    with Image.open(sys.argv[1]) as image:
        with Image.open("shirt.png") as shirt:
            shirt_size = shirt.size
            photo = ImageOps.fit(image, shirt_size)
            photo.paste(shirt, (0, 0), shirt)
            photo.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")

