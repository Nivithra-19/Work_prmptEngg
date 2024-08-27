import random

def guess_the_number():
    # Step 1: Initialize the game
    number_to_guess = random.randint(1, 100)
    max_guesses = 10
    guesses_taken = 0
    
    print("Welcome to 'Guess the Number' game!")
    print("I have chosen a number between 1 and 100. Can you guess what it is?")
    
    # Step 2: Start the game loop
    while guesses_taken < max_guesses:
        try:
            guess = int(input(f"Enter your guess ({max_guesses - guesses_taken} guesses left): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        guesses_taken += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {guesses_taken} tries.")
            break
    else:
        print(f"Sorry, you've run out of guesses. The number was {number_to_guess}.")
    
    # Step 3: End the game
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thank you for playing! Goodbye.")

# Start the game for the first time
guess_the_number()
