def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not check_length(s):
        return False

    if not check_punctuation(s):
        return False

    if not check_first_two_letters(s):
        return False
    
    if not check_numbers(s) :
        return False
  
    return True  
  
def check_length(s):
    return 2<= len(s) <=6

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
    
if __name__ == "__main__":
    main()