import random
import math

if __name__ == "__main__":
    #Declared variables for the game
    loop = False
    guess_number = 0
    guess_attemp = 0
    minimun_attemp = 0
    winner = False
    print("Welcome to the Number guessing Game")
    print("Introduce the range of the numbers to the game")
    print("-"*15)
    while loop != True:
        first_number = int(input("Please introduce the lower number: "))
        print("-"*15)
        second_number = int(input("Please introduce the upper number: "))
        print("-"*15)
        if first_number <= 0:
            print("The input numbers need to be more than zero")
        elif first_number > second_number:
            print("The first number need to be less than the second number")
        elif first_number == second_number:
            print("Both numbers need to be different")
        else:    
            loop = True

    winner_number = random.randint(first_number,second_number)
    minimun_attemp = round(math.log2(second_number-first_number+1))
    while guess_attemp != minimun_attemp:
        guess_number = int(input("Please introduce your guess: "))
        print("-"*15)
        if guess_number == winner_number:
            winner = True
            break
        elif guess_number > winner_number:
            print("Try Again! You guessed too high")
            print("-"*15)
            guess_attemp += 1
        elif guess_number < winner_number:
            print("Try Again! You guessed too small")
            print("-"*15)
            guess_attemp += 1
    
    if winner:
        print(f"Congratulations! You did it in ${guess_attemp} tries") 
    else:
        print("Better Luck Next Time!")