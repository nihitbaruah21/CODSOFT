def calculator():
    print("Simple Calculator")

    # Step 1: Get numbers from user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Step 2: Get operation choice
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter operation (+, -, *, /): ")

    # Step 3: Perform calculation
    if operation == "+":
        result = num1 + num2
        op = "Addition"
    elif operation == "-":
        result = num1 - num2
        op = "Subtraction"
    elif operation == "*":
        result = num1 * num2
        op = "Multiplication"
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        op = "Division"
    else:
        print("Invalid operation.")
        return

    # Step 4: Show result
    print(f"\n{op} of {num1} and {num2} is: {result}")

# Run the calculator
calculator()
