#Take input from user until enters cntrl D
#If input is not in dict catch valuerror 
#pass exception to again ask input
#convert user input to istitle() than map in dict
#after each input add the cost of item to total amount
#format total amount to .2f and add a prefix $ 


items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main() :
    total_amount = 0
    while True : 
        try :
            value = input("Item : ")
            value= value.title()
            #End of life error in windows work by ctrl Z
        except EOFError : 
            break
        else:
            if value in items : 
                total_amount += items[value]
                print(f"Total amount : ${total_amount :.2f}")             
             
main()
            