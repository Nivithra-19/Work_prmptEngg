import time
import random

def intro():
    """Introduction to the game"""
    print("\nWelcome to the Text Adventure Game!")
    print("You find yourself in a mysterious mansion.")
    print("Your goal is to find the hidden treasure.")
    print("Explore the mansion and choose wisely!")
    time.sleep(2)

def choose_path():
    """Function to choose a path"""
    print("\nYou are at a crossroads. Which path will you take?")
    print("1. Go left")
    print("2. Go right")
    print("3. Go straight")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        go_left()
    elif choice == '2':
        go_right()
    elif choice == '3':
        go_straight()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choose_path()

def go_left():
    """Path when going left"""
    print("\nYou chose to go left.")
    print("You enter a dark room.")
    time.sleep(1)
    print("There's a trap door beneath you!")
    print("You fell into a dungeon and lost the game.")
    play_again()

def go_right():
    """Path when going right"""
    print("\nYou chose to go right.")
    print("You enter a room filled with poisonous gas.")
    time.sleep(1)
    print("You manage to escape the room.")
    time.sleep(1)
    
    # Random chance of finding the treasure or encountering a trap
    if random.random() < 0.5:
        print("You found the treasure! Congratulations!")
    else:
        print("You triggered a trap and lost the game.")
    
    play_again()

def go_straight():
    """Path when going straight"""
    print("\nYou chose to go straight.")
    print("You find yourself in a library.")
    time.sleep(1)
    print("There are many books here.")
    time.sleep(1)
    print("You find a clue written in an old book.")
    time.sleep(1)
    print("It leads you to another room.")
    choose_path()

def play_again():
    """Ask if the player wants to play again"""
    play = input("\nDo you want to play again? (yes/no): ").lower()
    if play == "yes":
        start_game()
    else:
        print("Thank you for playing!")

def start_game():
    """Start the game"""
    intro()
    choose_path()

# Start the game
start_game()
