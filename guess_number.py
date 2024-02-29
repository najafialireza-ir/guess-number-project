# 1) input low number and high number
# 2) random : [a, b]
# 3) loop -> codition -> guess_number = 5 -> feedback

import random


try:
    low = int(input('Enter a low number: '))
    high = int(input('Enter a high number: '))
except:
    print("please enter a valid number...")


r = random.randint(low, high)    

guess_count = 5


while guess_count > 0:
    
    """get user guess and check item this loop
    """
    
    try:
        new_guess_str = input(f"remaindeguess:{guess_count} => Enter next guess: ")
        new_guess = int(new_guess_str)
        
        if r == new_guess:
            print("Great!, your guess is correct.")
            break
        
        elif r > new_guess:
            print("selected number lower than.")
        else: 
            print("selected number high than")
            
        guess_count -= 1
    except:
        print("please enter a valid number...")    
        