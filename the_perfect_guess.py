import random

def get_valid_number(prompt):
    """Ask user until they enter a valid integer"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Please enter a valid number.")

def play_game(max_number):
    """Play one round and return number of guesses"""
    secret = random.randint(1, max_number)
    guesses = 0
    print(f"🤖 I've chosen a number between 1 and {max_number}. Can you guess it?")

    while True:
        guess = get_valid_number("🔢 Enter your guess: ")
        guesses += 1

        if guess == secret:
            print(f"🎉 Correct! You guessed it in {guesses} guesses.")
            return guesses
        elif guess > secret:
            if guess - secret > max_number // 4:
                print("📉 Too high! Try a much smaller number.")
            else:
                print("📉 A bit high! Try slightly lower.")
        else:
            if secret - guess > max_number // 4:
                print("📈 Too low! Try a much bigger number.")
            else:
                print("📈 A bit low! Try slightly higher.")

def main():
    print("🎯 Welcome to The Perfect Guess Game!")
    best_score = None

    while True:
        print("\nChoose difficulty:")
        print("1️⃣ Easy (1–50)")
        print("2️⃣ Medium (1–100)")
        print("3️⃣ Hard (1–200)")
        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            max_number = 50
        elif choice == '2':
            max_number = 100
        elif choice == '3':
            max_number = 200
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")
            continue

        guesses = play_game(max_number)

        if best_score is None or guesses < best_score:
            best_score = guesses
            print(f"🏆 New best score: {best_score} guesses!")

        play_again = input("🔁 Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing! See you next time!")
            break

if __name__ == "__main__":
    main()
