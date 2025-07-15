import tkinter as tk

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Window setup
root = tk.Tk()
root.title("Simple Calculator")

# Entry field
entry = tk.Entry(root, width=25, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons dynamically
row = 1
col = 0
for b in buttons:
    action = lambda x=b: click(x) if x not in ['C', '='] else clear() if x == 'C' else calculate()
    tk.Button(root, text=b, width=5, height=2, font=('Arial', 14), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()