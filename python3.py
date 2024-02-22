import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        # Length of the password
        self.length_label = tk.Label(master, text="Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Complexity options
        self.complexity_label = tk.Label(master, text="Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")
        self.complexity_options = ["Low", "Medium", "High"]
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, *self.complexity_options)
        self.complexity_menu.grid(row=1, column=1, padx=10, pady=10)

        # Checkbox for security rules
        self.security_var = tk.BooleanVar()
        self.security_checkbutton = tk.Checkbutton(master, text="Adhere to security rules", variable=self.security_var)
        self.security_checkbutton.grid(row=2, columnspan=2, padx=10, pady=10)

        # Button to generate password
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, columnspan=2, padx=10, pady=10)

        # Display generated password
        self.password_label = tk.Label(master, text="")
        self.password_label.grid(row=4, columnspan=2, padx=10, pady=10)

        # Button to copy password to clipboard
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=5, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = self.length_entry.get()
        try:
            length = int(length)
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Length must be a positive integer.")
            return

        complexity = self.complexity_var.get()

        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "High":
            characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

        password = ''.join(random.choice(characters) for _ in range(length))

        if self.security_var.get():
            if not any(char.isupper() for char in password):
                password += random.choice(string.ascii_uppercase)
            if not any(char.islower() for char in password):
                password += random.choice(string.ascii_lowercase)
            if not any(char.isdigit() for char in password):
                password += random.choice(string.digits)
            if not any(char in string.punctuation for char in password):
                password += random.choice(string.punctuation)

            password = ''.join(random.sample(password, len(password)))

        self.password_label.config(text=password)

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "No password generated yet.")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
