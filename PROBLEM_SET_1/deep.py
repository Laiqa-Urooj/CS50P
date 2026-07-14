#Main function to ask user input
def main() :
    question=input("What is the answer to Great Question of Life, the Universe , and Everything ?")
    answer(question)
    
#Function to match user's answer and give answer
def answer(question):
    question = question.strip().lower()
    match question:
        case "forty two" | "forty-two" | "42":
            print("Yes")
        case _:
            print("No")

#Calling main function
main()

#We can also use in keyword 