def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        print("Error: Cannot calculate modulus with zero.")
        return None
    return a % b

def exponentiate(a, b):
    return a ** b

def calculator():
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting the calculator.")
            break

        try:
            a = float(input("Enter the first operand: "))
            b = float(input("Enter the second operand: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == '1':
            result = add(a, b)
        elif choice == '2':
            result = subtract(a, b)
        elif choice == '3':
            result = multiply(a, b)
        elif choice == '4':
            result = divide(a, b)
        elif choice == '5':
            result = modulus(a, b)
        elif choice == '6':
            result = exponentiate(a, b)
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue

        if result is not None:
            print(f"Result: {result}")
