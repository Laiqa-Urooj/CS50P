#Main function to take user's greeting 
def main() :
    greeting=input("How you doing ?")
    compensation(greeting)

#Function to calculate appropriate compensation for user's greeting
def compensation(message) :
    message=message.strip().lower()
    if message == "hello":
        print("$0")
    elif message.startswith("h"):
        print("$20")
    else:
        print("$100")

main()