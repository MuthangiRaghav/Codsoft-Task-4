import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_result(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("\n🎮 Welcome to Rock-Paper-Scissors Game! 🎮")

    while True:
        print("\nChoose one: Rock | Paper | Scissors (or type 'exit' to quit)")
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == "exit":
            print("\n🏁 Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! ✌️")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid input! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")

        result = get_result(user_choice, computer_choice)
        print(f"🧾 Result: {result}")

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"📊 Score - You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
