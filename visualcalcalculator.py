import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

# Creating the GUI window
root = tk.Tk()
root.title("Visual Python Calculator")

# Entry widget for input
entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button creation function
def create_button(text, row, col, width=7, height=2, command=None):
    button = tk.Button(root, text=text, width=width, height=height, font=("Arial", 14))
    button.grid(row=row, column=col, padx=5, pady=5)
    if command:
        button.config(command=command)
    else:
        button.config(command=lambda: entry.insert(tk.END, text))

# Adding number buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        create_button(text, row, col, command=evaluate_expression)
    else:
        create_button(text, row, col)

# Clear button
clear_button = tk.Button(root, text="Clear", width=7, height=2, font=("Arial", 14), command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Backspace button
back_button = tk.Button(root, text="Back", width=7, height=2, font=("Arial", 14), command=lambda: entry.delete(len(entry.get())-1, tk.END))
back_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Running the GUI loop
root.mainloop()
