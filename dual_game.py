import random

def get_user_choice(name, choices):
    while True:
        choice = input(f"{name}, choose {choices} (or 'q' to quit): ").lower()
        if choice in choices or choice == 'q':
            return choice
        print(f"❗ Invalid choice. Please choose from {choices}.")

def decide_winner(user1, user2, win_rules):
    if user1 == user2:
        return 'tie'
    elif (user1, user2) in win_rules:
        return 'user1'
    else:
        return 'user2'

def play_vs_computer(game_name, choices, win_rules, emoji_map):
    print(f"\n=== {game_name} 🤖 vs 👤 ===")
    score = {'win':0, 'lose':0, 'tie':0}

    while True:
        user = get_user_choice("👤 You", choices)
        if user == 'q':
            print("👋 Thanks for playing! Final score:", score)
            break
        comp = random.choice(choices)
        result = decide_winner(user, comp, win_rules)

        print(f"👤 You chose: {emoji_map.get(user, user)}")
        print(f"🤖 Computer chose: {emoji_map.get(comp, comp)}")

        if result == 'tie':
            print("🤝 It's a tie!")
            score['tie'] +=1
        elif result == 'user1':
            print("🎉 You win!")
            score['win'] +=1
        else:
            print("😢 You lose!")
            score['lose'] +=1

        print(f"📊 Score so far: {score}\n")

def play_vs_friend(game_name, choices, win_rules, emoji_map):
    print(f"\n=== {game_name} 👤 vs 👤 ===")
    score = {'Player 1':0, 'Player 2':0, 'tie':0}

    while True:
        user1 = get_user_choice("👤 Player 1", choices)
        if user1 == 'q':
            print("👋 Thanks for playing! Final score:", score)
            break
        user2 = get_user_choice("👤 Player 2", choices)
        if user2 == 'q':
            print("👋 Thanks for playing! Final score:", score)
            break

        result = decide_winner(user1, user2, win_rules)

        print(f"👤 Player 1 chose: {emoji_map.get(user1, user1)}")
        print(f"👤 Player 2 chose: {emoji_map.get(user2, user2)}")

        if result == 'tie':
            print("🤝 It's a tie!")
            score['tie'] +=1
        elif result == 'user1':
            print("🎉 Player 1 wins this round!")
            score['Player 1'] +=1
        else:
            print("🎉 Player 2 wins this round!")
            score['Player 2'] +=1

        print(f"📊 Score so far: {score}\n")

def main():
    print("🎮 Choose game mode:")
    print("1️⃣ – 🪨📄✂️ Stone Paper Scissors")
    print("2️⃣ – 🐍💧🔫 Snake Water Gun")
    mode = input("Enter 1 or 2: ").strip()

    if mode == '1':
        game_name = "🪨📄✂️ Stone Paper Scissors"
        choices = ['stone', 'paper', 'scissors']
        emoji_map = {'stone': '🪨', 'paper': '📄', 'scissors': '✂️'}
        win_rules = [('stone', 'scissors'), ('scissors', 'paper'), ('paper', 'stone')]
    elif mode == '2':
        game_name = "🐍💧🔫 Snake Water Gun"
        choices = ['snake', 'water', 'gun']
        emoji_map = {'snake': '🐍', 'water': '💧', 'gun': '🔫'}
        win_rules = [('snake', 'water'), ('water', 'gun'), ('gun', 'snake')]
    else:
        print("❗ Invalid choice. Exiting.")
        return

    print("\n🤔 Choose opponent:")
    print("c – 🤖 Play vs Computer")
    print("f – 👥 Play vs Friend")
    opponent = input("Enter c or f: ").strip().lower()

    if opponent == 'c':
        play_vs_computer(game_name, choices, win_rules, emoji_map)
    elif opponent == 'f':
        play_vs_friend(game_name, choices, win_rules, emoji_map)
    else:
        print("❗ Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
