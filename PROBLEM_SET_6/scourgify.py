import sys
import os
import csv



def main() :
    if len(sys.argv) <3 :
        sys.exit("Too few arguments")
    elif len(sys.argv) >3 :
        sys.exit("Too many arguments") 
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        validate(file1,file2)
        scourgify(file1,file2)

def validate(file1,file2) :
    if not file1.endswith('.csv') or not file2.endswith(".csv") :
        sys.exit("Not a csv file")
    if  not os.path.exists(file1) :
       sys.exit("No such file")
       
def scourgify(file1,file2) :
    with open(file1, newline="") as before ,open(file2,"w", newline="") as after :
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after,fieldnames=["first","last","house"])
        writer.writeheader()
        for row in reader :
            last,first = row["name"].split(", ")
            writer.writerow({
                "first" : first ,
                "last" : last ,
                "house" : row["house"]
            })
         
if __name__ == "__main__":
    main()