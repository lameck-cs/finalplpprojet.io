import tkinter as tk
from tkinter import messagebox
import math

# Calculator class
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enhanced Python Calculator")
        self.geometry("500x700")
        self.configure(bg="lightgray")
        
        # Store current expression and result
        self.expression = ""
        self.result_var = tk.StringVar()

        # Create the display
        self.create_display()

        # Create the buttons
        self.create_buttons()

    def create_display(self):
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), borderwidth=5, relief="sunken", justify="right", bd=10)
        display.grid(row=0, column=0, columnspan=5, padx=10, pady=20, sticky="we")
        self.result_var.set("0")
    
    def create_buttons(self):
        # Define button labels and their grid positions
        buttons = [
            ('C', 1, 0), ('M+', 1, 1), ('M-', 1, 2), ('%', 1, 3), ('bin', 1, 4),
            ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('sqrt', 2, 3), ('hex', 2, 4),
            ('asin', 3, 0), ('acos', 3, 1), ('atan', 3, 2), ('^', 3, 3), ('ln', 3, 4),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3), ('log', 4, 4),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
            ('0', 7, 0), ('.', 7, 1), ('+/-', 7, 2), ('+', 7, 3), ('=', 7, 4)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self, text=text, width=5, height=2, font=("Arial", 18), bg="lightblue", command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="we")

    def on_button_click(self, text):
        if text == "=":
            self.calculate_result()
        elif text == "C":
            self.clear()
        elif text == "M+":
            self.memory_store()
        elif text == "M-":
            self.memory_recall()
        elif text == "+/-":
            self.toggle_sign()
        elif text == "sqrt":
            self.square_root()
        elif text == "^":
            self.append_operator("**")
        elif text == "sin":
            self.calculate_trig("sin")
        elif text == "cos":
            self.calculate_trig("cos")
        elif text == "tan":
            self.calculate_trig("tan")
        elif text == "asin":
            self.calculate_inverse_trig("asin")
        elif text == "acos":
            self.calculate_inverse_trig("acos")
        elif text == "atan":
            self.calculate_inverse_trig("atan")
        elif text == "ln":
            self.calculate_ln()
        elif text == "log":
            self.calculate_log()
        elif text == "bin":
            self.convert_to_binary()
        elif text == "hex":
            self.convert_to_hex()
        else:
            self.append_operator(text)

    def append_operator(self, op):
        if self.result_var.get() == "0":
            self.result_var.set(op)
        else:
            self.result_var.set(self.result_var.get() + op)

    def calculate_result(self):
        try:
            expression = self.result_var.get()
            result = eval(expression)
            self.result_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression")

    def clear(self):
        self.result_var.set("0")
    
    def memory_store(self):
        self.memory = self.result_var.get()
    
    def memory_recall(self):
        self.result_var.set(self.memory)
    
    def toggle_sign(self):
        current = self.result_var.get()
        if current.startswith('-'):
            self.result_var.set(current[1:])
        else:
            self.result_var.set('-' + current)

    def square_root(self):
        try:
            value = float(self.result_var.get())
            self.result_var.set(math.sqrt(value))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for square root")

    def calculate_trig(self, func):
        try:
            value = float(self.result_var.get())
            radians = math.radians(value)  # Convert degrees to radians
            if func == "sin":
                self.result_var.set(math.sin(radians))
            elif func == "cos":
                self.result_var.set(math.cos(radians))
            elif func == "tan":
                self.result_var.set(math.tan(radians))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input for {func}")

    def calculate_inverse_trig(self, func):
        try:
            value = float(self.result_var.get())
            if func == "asin":
                self.result_var.set(math.degrees(math.asin(value)))
            elif func == "acos":
                self.result_var.set(math.degrees(math.acos(value)))
            elif func == "atan":
                self.result_var.set(math.degrees(math.atan(value)))
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input for {func}")

    def calculate_ln(self):
        try:
            value = float(self.result_var.get())
            self.result_var.set(math.log(value))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for ln")

    def calculate_log(self):
        try:
            value = float(self.result_var.get())
            self.result_var.set(math.log10(value))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for log")

    def convert_to_binary(self):
        try:
            value = int(self.result_var.get())
            self.result_var.set(bin(value)[2:])
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for binary conversion")

    def convert_to_hex(self):
        try:
            value = int(self.result_var.get())
            self.result_var.set(hex(value)[2:].upper())
        except Exception as e:
            messagebox.showerror("Error", "Invalid input for hexadecimal conversion")


if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
