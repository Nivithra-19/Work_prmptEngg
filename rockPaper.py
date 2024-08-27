import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper()
        if user_input == 'R':
            return 'Rock'
        elif user_input == 'P':
            return 'Paper'
        elif user_input == 'S':
            return 'Scissors'
        else:
            print("Invalid input. Please try again.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
