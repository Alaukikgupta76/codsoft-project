import customtkinter as ctk
import json
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")


class TaskMasterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("✨ Task Wizard")
        self.geometry("520x565")
        self.resizable(False, False)
        self.todo_items = []

        # Entry for new items
        self.input_field = ctk.CTkEntry(self, width=320, placeholder_text="What's your next mission?")
        self.input_field.place(x=36, y=20)

        # Add Task Button
        add_button = ctk.CTkButton(self, text="➕ New", command=self.handle_add)
        add_button.place(x=375, y=20)

        # Bulk Delete Button
        reset_button = ctk.CTkButton(self, text="🧹 Reset List", fg_color="#c0392b", command=self.remove_all)
        reset_button.place(x=385, y=505)

        # Main area for showing items
        self.list_frame = ctk.CTkScrollableFrame(self, width=445, height=430)
        self.list_frame.place(x=36, y=70)

        self.load_file()
        self.show_items()

    def handle_add(self):
        item_txt = self.input_field.get().strip()
        if item_txt:
            self.todo_items.append({"mission": item_txt, "done": False})
            self.input_field.delete(0, 'end')
            self.save_file()
            self.show_items()

    def toggle_done(self, idx):
        self.todo_items[idx]["done"] = not self.todo_items[idx]["done"]
        self.save_file()
        self.show_items()

    def delete_item(self, idx):
        self.todo_items.pop(idx)
        self.save_file()
        self.show_items()

    def remove_all(self):
        self.todo_items = []
        self.save_file()
        self.show_items()

    def show_items(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for idx, item in enumerate(self.todo_items):
            row = ctk.CTkFrame(self.list_frame)
            row.pack(padx=7, pady=7, fill="x")

            status_col = "#4ed693" if item["done"] else "#f05454"
            txt = f"🟢 {item['mission']}" if item["done"] else f"⚪ {item['mission']}"

            info_label = ctk.CTkLabel(row, text=txt, text_color=status_col, anchor="w")
            info_label.pack(side="left", padx=15, fill="x", expand=True)
            info_label.bind("<Button-1>", lambda e, i=idx: self.toggle_done(i))

            del_button = ctk.CTkButton(row, text="❎", width=34, fg_color="#a5011a", command=lambda i=idx: self.delete_item(i))
            del_button.pack(side="right", padx=4)

    def save_file(self):
        with open("wizard_tasks.json", "w") as f:
            json.dump(self.todo_items, f, indent=3)

    def load_file(self):
        if os.path.exists("wizard_tasks.json"):
            with open("wizard_tasks.json", "r") as f:
                self.todo_items = json.load(f)


if __name__ == "__main__":
    app = TaskMasterApp()
    app.mainloop()
