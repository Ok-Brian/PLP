import tkinter as tk
from tkinter import messagebox

# Function to check leap year
def check_leap_year():
    year_str = entry.get()
    if not year_str.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid year.")
        return

    year = int(year_str)

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = f"{year} is a leap year."
    else:
        result = f"{year} is not a leap year."

    messagebox.showinfo("Result", result)

# Set up GUI window
root = tk.Tk()
root.title("Leap Year Checker")
root.geometry("300x150")

# Input label
label = tk.Label(root, text="Enter a year:")
label.pack(pady=5)

# Input field
entry = tk.Entry(root)
entry.pack(pady=5)

# Check button
check_button = tk.Button(root, text="Check", command=check_leap_year)
check_button.pack(pady=10)

# Run the app
root.mainloop()
#Hahahaaa this my first Tkinter project.Beautiful af bruv!!!!😂
