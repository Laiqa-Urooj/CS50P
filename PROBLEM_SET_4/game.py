#ask user for a positive integer --done
#if the number not positive ask again..use while--done
#random.int to generate a number from 1 to positive int --done
#ask the user to take a guess until positive guess entered
#compare guess with randint and give hhints to user
#until correctly guessed


import random
def main() :
    while True :
        try:
            n = int(input("Level: "))
            if n > 0 :
                num = random.randint(1,n)
                while True :
                    try:
                        guess = int(input("Guess: "))
                        if guess > 0 :
                            if guess == num :
                                print("Just right!")
                                return
                            elif guess > num :
                                print("Too large!")
                            else:
                                print("Too small!")
                        else:
                            continue
                    except ValueError :
                        continue
                        
                
        except ValueError :
            continue
    
    
    
main()