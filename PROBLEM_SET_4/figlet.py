#cli expects 0 or 2 arguments
#if 0 arguments output text in a random font
#else  if 2 arguments 
#only if the first argument of 2 is -f or --font and
#2nd argument is an existing font
#output in that specific font
#if any of the 2 argument is not correct exit via sys.exit
#ask user for a string of text
#output text in desired font
#exit program


from pyfiglet import Figlet
import random
import sys


def main():
    figlet = Figlet()

    # Get all available fonts
    fonts = figlet.getFonts()

    # Program accepts either:
    # python figlet.py
    # or
    # python figlet.py -f slant

    if len(sys.argv) == 1:
        # Choose a random font
        figlet.setFont(font=random.choice(fonts))

    elif len(sys.argv) == 3:
        # Validate first argument
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        # Validate font name
        if sys.argv[2] not in fonts:
            sys.exit("Invalid usage")

        # Set the requested font
        figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("Invalid usage")

    # Ask user for text
    text = input("Input: ")

    # Render and print text
    print(figlet.renderText(text))


main()