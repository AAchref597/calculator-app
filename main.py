from calculator import Calculator

calc = Calculator()

while True:
    print("\n=== CALCULATOR ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose operation: ")

    if choice == "5":
        print("Goodbye!")
        break

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", calc.add(a, b))

        elif choice == "2":
            print("Result:", calc.subtract(a, b))

        elif choice == "3":
            print("Result:", calc.multiply(a, b))

        elif choice == "4":
            print("Result:", calc.divide(a, b))

        else:
            print("Invalid choice, try again.")

    except ValueError:
        print("Error: Please enter valid numbers.")
