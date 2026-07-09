from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

text = input("Input: ")

if len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
else:
    figlet.setFont(font=random.choice(figlet.getFonts()))

print(figlet.renderText(text))