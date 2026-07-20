# def hy() :
#     """This is a docstring """
#     print("hello")

# hy()
# print(hy.__doc__)
# print(dir(sys.argv))

#Take 1 cli 
#if less arg print too few sys.exit
#if more arg print too many sys.exit
#Check if arg name ends with .py
#if not not a py file and sys.exit
#if ends with .py check if file exists
#if does not exit sys.exit
#if exists 
#open the file
#ignore comments 
#count the number of lines in file 
#output the number of files in int

import os
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    filename = sys.argv[1]
    validate(filename)
    print(count_lines(filename))

def validate(filename):
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    if not os.path.exists(filename):
        sys.exit("File does not exist")

def count_lines(filename):
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("#"):
                continue
            count += 1
    return count

if __name__ == "__main__":
    main()