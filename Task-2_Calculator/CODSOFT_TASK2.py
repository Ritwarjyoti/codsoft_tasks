print("===== SIMPLE CALCULATOR =====")

print("\nAvailable Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nWhich operation do you want to perform? ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

match choice:
    case "1":
        result = num1 + num2
        print("\nResult:", result)

    case "2":
        result = num1 - num2
        print("\nResult:", result)

    case "3":
        result = num1 * num2
        print("\nResult:", result)

    case "4":
        if num2 == 0:
            print("\nError! Division by zero is not possible.")
        else:
            result = num1 / num2
            print("\nResult:", result)

    case _:
        print("\nInvalid operation! Please select between 1 and 4.")
