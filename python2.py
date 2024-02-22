import tkinter as tk
from tkinter import messagebox

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        # Labels
        self.label_weight = tk.Label(master, text="Weight (kg):")
        self.label_weight.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.label_height = tk.Label(master, text="Height (m):")
        self.label_height.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Entry widgets
        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10)

        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=1, column=1, padx=10, pady=10)

        # Button to calculate BMI
        self.calculate_button = tk.Button(master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Result label
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive values.")
                return

            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)
            result_text = f"Your BMI is: {bmi:.2f}\nYou are classified as: {category}"
            self.result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

def main():
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
