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
    print("4. Go upstairs")
    print("5. Go downstairs")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        go_left()
    elif choice == '2':
        go_right()
    elif choice == '3':
        go_straight()
    elif choice == '4':
        go_upstairs()
    elif choice == '5':
        go_downstairs()
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        choose_path()

def go_left():
    """Path when going left"""
    print("\nYou chose to go left.")
    print("You enter a dark room.")
    time.sleep(1)
    print("There's a flickering light. Do you want to investigate?")
    choice = input("Enter your choice (yes/no): ").lower()
    
    if choice == 'yes':
        print("You approach the light and discover a hidden passage!")
        time.sleep(1)
        print("The passage leads you to a room full of ancient artifacts.")
        choose_artifact()
    else:
        print("You decide not to investigate and turn back.")
        choose_path()

def go_right():
    """Path when going right"""
    print("\nYou chose to go right.")
    print("You enter a room with three doors.")
    time.sleep(1)
    print("Which door do you choose?")
    print("1. Red door")
    print("2. Blue door")
    print("3. Green door")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        print("The red door leads to a room filled with poisonous gas. Game over!")
        play_again()
    elif choice == '2':
        print("The blue door reveals a safe passage. You continue your journey.")
        choose_path()
    elif choice == '3':
        print("The green door opens to a garden maze. Can you find your way through?")
        if random.random() < 0.5:
            print("You successfully navigate the maze and find a golden key!")
            time.sleep(1)
            print("The key might be useful later.")
            global golden_key
            golden_key = True
            choose_path()
        else:
            print("You get lost in the maze and can't find your way out. Game over!")
            play_again()
    else:
        print("Invalid choice. You hesitate and trigger a trap. Game over!")
        play_again()

def go_straight():
    """Path when going straight"""
    print("\nYou chose to go straight.")
    print("You find yourself in a library.")
    time.sleep(1)
    print("There are many books here. Do you want to read one?")
    choice = input("Enter your choice (yes/no): ").lower()
    
    if choice == 'yes':
        if random.random() < 0.7:
            print("You find a clue in the book!")
            time.sleep(1)
            print("It leads you to another room.")
            choose_path()
        else:
            print("The book triggers a trap! You're trapped in the library forever. Game over!")
            play_again()
    else:
        print("You decide not to read and continue exploring.")
        choose_path()

def go_upstairs():
    """Path when going upstairs"""
    print("\nYou chose to go upstairs.")
    print("You find yourself on a balcony overlooking a courtyard.")
    time.sleep(1)
    print("You see a glint of something shiny in the courtyard.")
    print("Do you want to try to reach it or continue exploring upstairs?")
    choice = input("Enter your choice (reach/explore): ").lower()
    
    if choice == 'reach':
        if random.random() < 0.4:
            print("You successfully retrieve the shiny object. It's the treasure! You win!")
            play_again()
        else:
            print("You lose your balance and fall. Game over!")
            play_again()
    else:
        print("You continue exploring upstairs and find a mysterious locked door.")
        if 'golden_key' in globals() and golden_key:
            print("You use the golden key to open the door and find the treasure! You win!")
            play_again()
        else:
            print("You can't open the door. You'll need to find a key.")
            choose_path()

def go_downstairs():
    """Path when going downstairs"""
    print("\nYou chose to go downstairs.")
    print("You enter a dimly lit cellar.")
    time.sleep(1)
    print("You hear strange noises. Do you want to investigate?")
    choice = input("Enter your choice (yes/no): ").lower()
    
    if choice == 'yes':
        if random.random() < 0.6:
            print("You find a friendly ghost who gives you a clue!")
            time.sleep(1)
            print("The ghost mentions a hidden passage in the library.")
            choose_path()
        else:
            print("The noise was a trap! You're caught and the game is over.")
            play_again()
    else:
        print("You decide not to investigate and return upstairs.")
        choose_path()

def choose_artifact():
    """Function to choose an artifact"""
    print("\nYou see three artifacts. Which one do you choose?")
    print("1. A golden compass")
    print("2. An old map")
    print("3. A mysterious amulet")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        print("The golden compass points you towards the treasure!")
        print("Congratulations! You've won the game!")
        play_again()
    elif choice == '2':
        print("The old map reveals a secret passage!")
        choose_path()
    elif choice == '3':
        print("The mysterious amulet teleports you to a random location.")
        choose_path()
    else:
        print("Invalid choice. The artifacts disappear and you must continue without them.")
        choose_path()

def play_again():
    """Ask if the player wants to play again"""
    play = input("\nDo you want to play again? (yes/no): ").lower()
    if play == "yes":
        global golden_key
        golden_key = False
        start_game()
    else:
        print("Thank you for playing!")
        exit()

def start_game():
    """Start the game"""
    intro()
    choose_path()

# Start the game
golden_key = False
start_game()