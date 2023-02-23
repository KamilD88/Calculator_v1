import tkinter as tk

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = tk.Entry(master, width=25, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Define buttons
        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        # Create buttons
        for button in self.buttons:
            text, row, col = button
            tk.Button(
                master, text=text, width=5, font=('Arial', 14),
                command=lambda text=text: self.click_button(text)
            ).grid(row=row, column=col, padx=5, pady=5)

    def click_button(self, text):
        if text == 'C':
            self.entry.delete(0, tk.END)
        elif text == '=':
            self.calculate()
        else:
            self.entry.insert(tk.END, text)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")


root = tk.Tk()
calc_gui = CalculatorGUI(root)
root.mainloop()



class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

print("Calculator")

calc = Calculator()

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = calc.add(num1, num2)
elif choice == '2':
    result = calc.subtract(num1, num2)
elif choice == '3':
    result = calc.multiply(num1, num2)
elif choice == '4':
    try:
        result = calc.divide(num1, num2)
    except ValueError as e:
        print(e)
        exit()
else:
    print("Invalid input")
    exit()

print("Result: ", result)


