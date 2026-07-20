import sys
import os
import tabulate
import csv
def main() :
    if len(sys.argv) > 2 :
        sys.exit("Too many arguments")
    elif len(sys.argv) <2 :
        sys.exit("Too few arguments")
    else :
        filename = sys.argv[1]
        validate(filename)
        print(display_output(filename))

def validate(filename) :
    if not filename.endswith(".csv") :
        sys.exit("Not a csv file")
    if not os.path.exists(filename) :
        sys.exit("No such file") 

def display_output(filename) :
    with open(filename) as csvfile :
        data = csv.reader(csvfile)
        return tabulate.tabulate(data, headers= "firstrow", tablefmt="grid")

main()