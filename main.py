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
