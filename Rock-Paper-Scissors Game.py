import random


class RockPaperScissorsGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.choice_map = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}

    def display_menu(self):
        print("\nMake your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        selection = input("Enter 1 / 2 / 3: ")
        return self.choice_map.get(selection)

    def get_computer_choice(self):
        return random.choice(self.choices)

    def evaluate(self, player, computer):
        if player == computer:
            return "It's a Draw!"
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            return "You are the Champion!"
        else:
            return "The Computer is Victorious!"

    def play_round(self):
        player_choice = self.display_menu()
        if not player_choice:
            print("❌ Invalid input. Please try again.")
            return

        computer_choice = self.get_computer_choice()

        print(f"\n🧍 You chose: {player_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        result = self.evaluate(player_choice, computer_choice)
        print("🏁 Result:", result)

        if result == "You are the Champion!":
            self.player_score += 1
        elif result == "The Computer is Victorious!":
            self.computer_score += 1

        print(f"📊 Score — You: {self.player_score} | Computer: {self.computer_score}")

    def run(self):
        print("🎮 Welcome to Rock-Paper-Scissors!")
        while True:
            self.play_round()
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again != 'y':
                print("👋 Thanks for playing! Final Score:")
                print(f"🧍 You: {self.player_score} | 💻 Computer: {self.computer_score}")
                break


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()

