
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

    def menu(operator, numbers):
        match operator:
            case '+':
                return add(numbers)
            case '-':
                return subtract(numbers)
            case '/':
                return divide(numbers)
            case '*':
                return multiply(numbers)
    
    def add(numbers):
        return numbers [a] + [b]

    def subtract(numbers):
        return numbers [a] - [b]

    def divide(numbers):
        return numbers [a] / [b]

    def multiply(numbers):
        return numbers [a] * [b]


calc = menu(operator, a, b)
