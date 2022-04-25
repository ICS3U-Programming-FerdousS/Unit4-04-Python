# Created by: Ferdous Sediqi
# created by: Ferdous Sediqi
# Created on: April. 25, 2022
# In this program asks user guess a number (0-9)
# and then inside while loop check if user guessed right number or not
# if user guessed the right number stop program using break otherwise
# keep asking to guess a number


# import math random
import random

def main():
    # set random number between 0-9
    random_number = random.randint(0, 9)
    print("")

    # using while loop to keep asking user to guess a number
    while True:
        string_input = input("Enter a number 0-9 ")
        
        # cast user input from string to int
        try:
            integer_input = int(string_input)
            print("")
            # check if user guess is right or wrong
            if integer_input == random_number:
                print("You guessed it right!")
                break
            else:
                # display the right number if they guessed it wrong
                print("You guessed the wrong number.")
                continue
        # display invalid input 
        except Exception:
            print("")
            print( "Invalid input. Input was not an number.")
            continue

if __name__ == "__main__":
    main()
