import random

def welcome():
    """Display welcome message"""
    print("=" * 50)
    print("🎮 Welcome to Number Guessing Game! 🎮")
    print("=" * 50)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print("=" * 50)

def play_game():
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed = False
    
    while not guessed:
        guess = int(input("\nEnter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("📉 Too Low! Try a higher number.")
        elif guess > secret_number:
            print("📈 Too High! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            guessed = True

def main():
    welcome()
    play_game()

main()
