#using emoji module to convert text to emojis 



import emoji
def main() :
    normal_text = input("Input : ")
    emojized_text = emoji.emojize(normal_text,language = "alias")
    print(f"Output: {emojized_text}")
    
    
main()