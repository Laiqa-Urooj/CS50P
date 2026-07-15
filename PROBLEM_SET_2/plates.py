#first 2 characters must me alphabets
#maximum characters allowed are 6 and minimum allowed are 2
#numbers are allowed only at end 
#first number must be greater than 0
#periods,punctuation marks and spaces are not allowed
#functions return a value valid or invalid


#if length is less than or equal to 6 and greater than or equal to 2 process
#else return invalid
#if character is isalnum process
#else invalid
#if character at index 0 and 1 is isalpha ..than process
#else return invalid
#if character isdigit() and greater than 0 process

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not check_length(len(s)):
        return False

    if not check_punctuation(s):
        return False

    if not check_first_two_letters(s):
        return False
    
    if not check_numbers(s) :
        return False
  
    return True  
  
  
#Another way to return multiple values 
#     return (
#         check_length(len(s)) and
#    check_punctuation(s)
#     )
        

def check_length(s):
    return 2<= s <=6

def check_punctuation(s) :
    return s.isalnum()
  
def check_first_two_letters(s) :
    return s[0].isalpha() and s[1].isalpha()  

def check_numbers(s):
    seen_number = False
    for character in s:
        if character.isdigit():
            if not seen_number:
                if character == "0":
                    return False
                seen_number = True

        elif seen_number:
            return False

    return True
                  

main()