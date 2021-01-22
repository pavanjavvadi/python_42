#number guessing
import random

num = random.randint(1,100)
print("Hi,welcome to the Mathlogic.Have fun by playing this game.For help,I will provide you the clues.\nMaximun attempts : 5 ")
record = int(input("Enter any number between 1 and 100: "))  
attempts = 1
score = 10
max_attempts = 5
while True:
    def even_or_odd():
        if num%2 == 0:
            print("Clue 1: Computer guessed an even number.")
        else:
            print("Clue 1: Computer guessed an odd number.")
    def div_5():
        clue2 = num % 5
        print(f"Clue 2: If the number is divided by 5,then it leaves a remainder: {clue2}")
    def final_clue():
        num_str = str(num)
        print("Final clue: Number ends with : ",num_str[-1])

    if max_attempts <= 5 and max_attempts > 1:
        if num == record:
            print(f"Your guess matches with the computer in {attempts} attempts with score: {score}pts.")
            attempts = 1
            score = 10
            break
        
        elif num > record:
            max_attempts = max_attempts -1
            print(f"\nChoose a number which is greater than the previous number.\nRemaining attempts left:{max_attempts}")
            attempts = attempts + 1
            score = score - 1
            if attempts == 2:
                even_or_odd()
            elif attempts == 4:
                div_5()  
            elif attempts == 5:
                final_clue()      
            record = int(input("Enter any number between 1 and 100: "))
            
        elif num < record:
            max_attempts = max_attempts -1
            print(f"\nChoose a number which is lower than the previous number.\nRemaining attempts left:{max_attempts}")
            attempts = attempts + 1
            score = score - 1
            if attempts == 2:
                even_or_odd()
            elif attempts == 4:
                div_5()    
            elif attempts == 5:
                final_clue()    
            record = int(input("Enter any number between 1 and 100: "))
            
    else:
        print("\nMaximum attempts are reached. You lost the game.\nThe number which you missed:",num)
        break