#Take input until 50 cents are inserted assume it to be int
#Accepted denominations are 5 10 25 else ask question again and do not accept amount
#if more than 50 are inserted add excess to change owed else show 0
#end loop
#Function has to show change owed at last and amount due with  each insertion

def main() :
    calculate_price()
   
    
   
accepted_denominations = [5 ,10 ,25]
def calculate_price() :
    amount_due = 50
    while amount_due > 0:
        print(f"Amount due : {amount_due}")
        amount = int(input("Insert coin : "))
        if amount in accepted_denominations :
            amount_due -= amount                  
    print(f"Change owed: {-amount_due}")              
        
            
main()