import math

def calculator():
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Cannot divide by zero",
        '%': lambda x, y: x % y if y != 0 else "Cannot divide by zero",
        '**': lambda x, y: x ** y,
        '//': lambda x, y: x // y if y != 0 else "Cannot divide by zero",
        'abs': lambda x, y: abs(x - y),
        'max': lambda x, y: max(x, y),
        'min': lambda x, y: min(x, y),
        'pow': lambda x, y: pow(x, y),
        'sqrt': lambda x, _: math.sqrt(x) if x >= 0 else "Cannot take sqrt of negative number",
        'sin': lambda x, _: math.sin(math.radians(x)),
        'cos': lambda x, _: math.cos(math.radians(x)),
        'tan': lambda x, _: math.tan(math.radians(x)),
        'log': lambda x, _: math.log(x) if x > 0 else "Log undefined for non-positive numbers",
        'exp': lambda x, _: math.exp(x)
    }

    while True:
        try:
            num1 = float(input("\nEnter first number (or type 'q' to quit): "))
        except ValueError:
            print("Exiting calculator. Goodbye!")
            break

        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print("""
Choose operation:
+  -  *  /  %  **  //  abs  max  min  pow
sqrt  sin  cos  tan  log  exp
(For sqrt, sin, cos, tan, log, exp: only first number is used)
        """)
        op = input("Operation: ")

        if op in operators:
            result = operators[op](num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid operation. Please choose a correct one.")

# Run the calculator
calculator()