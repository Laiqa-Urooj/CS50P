def main() :
    camel_case = input("Camel Case : ")
    snake_case(camel_case)

def snake_case(text) :
    snake = ""
#Loops through each character to find the one which is upper case and converts it to lower case and adds _
    for c in text:
        if c.isupper() :
            snake += '_' + c.lower() 
        else:
            snake +=c
    return snake
            
main()