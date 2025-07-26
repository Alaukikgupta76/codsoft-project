import random
import string


class PasswordGenerator:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.symbols = string.punctuation

    def generate(self, length: int) -> str:
        """
        Generate a secure random password of given length.
        Ensures at least one letter, digit, and symbol.
        """
        if length < 4:
            return "❌ Password must be at least 4 characters long."

        # Ensure one of each type
        password_chars = [
            random.choice(self.letters),
            random.choice(self.digits),
            random.choice(self.symbols)
        ]

        # Fill remaining characters
        all_chars = self.letters + self.digits + self.symbols
        password_chars += random.choices(all_chars, k=length - 3)

        random.shuffle(password_chars)
        return ''.join(password_chars)

    def run(self):
        """Prompt the user for length and generate password."""
        print("\n🔐 Secure Password Generator 🔐")
        try:
            length = int(input("Enter the desired password length: "))
            password = self.generate(length)
            print(f"\n✅ Your Generated Password: {password}")
        except ValueError:
            print("\n⚠️ Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()
