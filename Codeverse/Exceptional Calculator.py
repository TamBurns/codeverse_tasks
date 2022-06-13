# Exceptional Calculator

# Write a Calculator class having methods to add, subtract, divide and multiply 2 numbers.
# Ensure that the methods throw appropriate exceptions.
# Finally, write a class CalculatorUser which makes use of this implementation and handles exceptions appropriately.

operator = input('''
Choose math operation:
+ to add
- to subtract
/ to divide
* to multipy
''')

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))


class Calculator:
    def __init__(self, operator, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def divide(self):
        return self.a / self.b

    def multiply(self):
        return self.a * self.b
      


calc = Calculator(operator, a, b)

if operator == '+':
    print(a + b)

elif operator == '-':
    print(a-b)

elif operator == '/':
    print(a / b)
    raise ZeroDivisionError("Cannot divide by 0")
    
elif operator == '*':
    print(a * b)
    
else:
    print("Operation not supported.")
         

