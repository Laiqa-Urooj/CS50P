#Taking input from user with an emoticon
def main():
    emoticon_string=input("Write a line of text with an emotion : ")
    #passing the argument and calling converting_emoticon function
    print(converting_emoticon(emoticon_string)) 

#Function to receive user input as argument and convert emoticons to emojis
def converting_emoticon(emoticon_string):
    converted_string=emoticon_string.replace(":)","🙂").replace(":(","🙁")
    return converted_string
    
#calls main function
main()


