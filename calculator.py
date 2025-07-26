import tkinter as tk


class BasicCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Basic Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)

        self.expression = ""

        self.create_display()
        self.create_buttons()

    def create_display(self):
        """Creates the input display area."""
        input_frame = tk.Frame(self.root, height=60, bg="lightblue")
        input_frame.pack(fill="both")

        self.display_var = tk.StringVar()

        display_entry = tk.Entry(
            input_frame,
            textvariable=self.display_var,
            font=("Helvetica", 24),
            bd=0,
            bg="white",
            justify="right"
        )
        display_entry.pack(expand=True, fill="both")

    def create_buttons(self):
        """Creates calculator buttons."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"],
        ]

        for row_values in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(expand=True, fill="both")

            for label in row_values:
                button = tk.Button(
                    row_frame,
                    text=label,
                    font=("Helvetica", 20),
                    height=2,
                    width=4,
                    command=lambda char=label: self.handle_input(char)
                )
                button.pack(side="left", expand=True, fill="both")

    def handle_input(self, char):
        """Processes user input."""
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                # Warning: eval is unsafe in general; for real apps, use safer parsing methods
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)

        self.display_var.set(self.expression)


# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = BasicCalculator(root)
    root.mainloop()
