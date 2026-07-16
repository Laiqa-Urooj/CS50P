#ask user for names until eof exception break ..done
#while loop for repeated asking name end when eof exception ..done
#store the names entered by user in a list --done
#iterate through names list --done
#join the words by commas and ands
#print the output strings



import inflect
p = inflect.engine()
# print(p.join(("apple"))) #if only 1 element than separates the letters

def main() :
    names = []
    while True :
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError :
            break
        
    bid_adieu(names)
            
    # print(names)
def bid_adieu(names) :
        name = p.join(names)
        print(f"Adieu, adieu, to {name}")
main()