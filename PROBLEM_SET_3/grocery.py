#ask user input repeatedly until eof exception ..break
#convert the users input to .upper()
#store the items in a dict .embed ..list ,methods
#sort and output the list by alphabet
#count frequency of each item in list and prefix that
#keyerror when a key is not found in the dictionary

items = {
    
}

def main() :
    while True :
        try :
            item = input("Item :")
            item = item.upper()
        # except KeyError :
        #     pass
        except EOFError :
            break
        else:
            if item in items:
                items[item] +=1
            else:
                items[item] = 1
    display(items)
   
#sorted does not change original list
#sort changes original list
def display(items) :
    for item in sorted(items) :
        print(items[item],item)
        
main()