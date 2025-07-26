import customtkinter as ctk
from tkinter import messagebox
import json
import os

# Appearance Settings
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

DATA_FILE = "contacts.json"


# ---------------------------
# Utility Functions
# ---------------------------
def load_contacts():
    """Loads contacts from a JSON file."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_contacts(data):
    """Saves contacts to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


# ---------------------------
# GUI Application Class
# ---------------------------
class ContactManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("📇 Contact Manager")
        self.geometry("700x450")
        self.resizable(False, False)

        self.contacts = load_contacts()
        self.init_ui()
        self.refresh_contacts()

    # ---------------------------
    # UI Setup
    # ---------------------------
    def init_ui(self):
        self.setup_input_fields()
        self.setup_search()
        self.setup_listbox()
        self.setup_buttons()

    def setup_input_fields(self):
        form_frame = ctk.CTkFrame(self)
        form_frame.pack(pady=10, padx=10, fill="x")

        self.name_entry = ctk.CTkEntry(form_frame, placeholder_text="Name")
        self.name_entry.grid(row=0, column=0, padx=5, pady=5)

        self.phone_entry = ctk.CTkEntry(form_frame, placeholder_text="Phone")
        self.phone_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_entry = ctk.CTkEntry(form_frame, placeholder_text="Email")
        self.email_entry.grid(row=1, column=0, padx=5, pady=5)

        self.address_entry = ctk.CTkEntry(form_frame, placeholder_text="Address")
        self.address_entry.grid(row=1, column=1, padx=5, pady=5)

        self.save_button = ctk.CTkButton(
            form_frame, text="➕ Add / Update", command=self.save_contact
        )
        self.save_button.grid(row=2, column=0, columnspan=2, pady=10)

    def setup_search(self):
        self.search_entry = ctk.CTkEntry(self, placeholder_text="🔍 Search by Name or Phone")
        self.search_entry.pack(pady=5, padx=10, fill="x")
        self.search_entry.bind("<KeyRelease>", self.search_contacts)

    def setup_listbox(self):
        self.contact_listbox = ctk.CTkTextbox(self, width=650, height=150)
        self.contact_listbox.pack(pady=5, padx=10)

    def setup_buttons(self):
        self.delete_button = ctk.CTkButton(
            self, text="🗑️ Delete Selected", fg_color="red", command=self.delete_contact
        )
        self.delete_button.pack(pady=10)

    # ---------------------------
    # Core Logic
    # ---------------------------
    def refresh_contacts(self, contacts=None):
        """Displays the current list of contacts."""
        self.contact_listbox.delete("0.0", "end")
        for contact in contacts or self.contacts:
            display = f"{contact['name']} - {contact['phone']}\n"
            self.contact_listbox.insert("end", display)

    def save_contact(self):
        """Adds or updates a contact."""
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("❌ Missing Info", "Name and Phone are required.")
            return

        # Update existing or add new
        updated = False
        for contact in self.contacts:
            if contact['phone'] == phone:
                contact.update({"name": name, "email": email, "address": address})
                updated = True
                break

        if not updated:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})

        save_contacts(self.contacts)
        self.refresh_contacts()
        self.clear_form()
        messagebox.showinfo("✅ Success", "Contact saved successfully.")

    def delete_contact(self):
        """Deletes a selected contact from the list."""
        try:
            selected = self.contact_listbox.get("sel.first", "sel.last").strip()
            name = selected.split(" - ")[0]

            self.contacts = [c for c in self.contacts if c["name"] != name]
            save_contacts(self.contacts)
            self.refresh_contacts()
            messagebox.showinfo("🗑️ Deleted", "Contact removed.")
        except Exception:
            messagebox.showerror("⚠️ Error", "Please select a contact to delete.")

    def search_contacts(self, event):
        """Search contacts based on query."""
        query = self.search_entry.get().strip().lower()
        if not query:
            self.refresh_contacts()
            return

        filtered = [c for c in self.contacts if query in c["name"].lower() or query in c["phone"]]
        self.refresh_contacts(filtered)

    def clear_form(self):
        """Clears all entry fields."""
        self.name_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')


# ---------------------------
# Run Application
# ---------------------------
if __name__ == "__main__":
    app = ContactManagerApp()
    app.mainloop()
