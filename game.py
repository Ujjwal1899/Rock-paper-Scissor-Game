import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock, Paper, Scissors Game!")
    print("Type 'quit' anytime to exit.\n")

    while True:
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()

        if user_choice == "quit":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! 👋")
            break

        if user_choice not in options:
            print("❌ Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Game logic
        if user_choice == computer_choice:
            print("😐 It's a Tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("✅ You Win!")
            user_score += 1
        else:
            print("💻 Computer Wins!")
            computer_score += 1

        # Show current score
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

# Run the game
play_game()
