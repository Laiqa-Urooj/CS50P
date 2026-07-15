#take input string from user
#iterate each character through the string
#if the character is vowel(a,e,i,o,u) remove it 
#add the non vowel characters to output string 
#print output

def main() :
    text = input("Input: ")
    output = omit_vowel(text)
    print(output)

def omit_vowel(text):
    vowels = "aeiouAEIOU"
    output=""
    for character in text :
        if character not in vowels :
            output += character         
    return output
        
main()