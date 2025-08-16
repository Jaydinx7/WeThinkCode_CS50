import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

# Random Font
if len(sys.argv) == 1:
    text = input("Input: ")
    f = Figlet(font=random.choice(fonts))

# Choose Font
elif len(sys.argv) == 3:
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = Figlet(font=sys.argv[2])
        text = input("Input: ")

    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")


print("Output:")
print(f.renderText(text))
