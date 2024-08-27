import random

def coin_toss():
    return "Heads" if random.choice([True, False]) else "Tails"

def main():
    print("Welcome to the Coin Toss Game!")
    wins = 0
    losses = 0

    while True:
        user_input = input("\nGuess the toss result (H for Heads/T for Tails) or type 'Q' to quit: ").upper()
        if user_input == 'Q':
            break
        elif user_input not in ['H', 'T']:
            print("Invalid input. Please guess 'H' for Heads or 'T' for Tails.")
            continue

        guess = "Heads" if user_input == 'H' else "Tails"
        result = coin_toss()
        print(f"The coin landed on {result}!")

        if guess == result:
            print("Congratulations, you guessed it right!")
            wins += 1
        else:
            print("Sorry, better luck next time.")
            losses += 1

        print(f"Total Wins: {wins}\nTotal Losses: {losses}")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
