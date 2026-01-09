import math

while True:
    print("\n=== Scientific Calculator ===")

    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Power (x^y)
    6. Square Root
    7. Square
    8. Sine (sin x)
    9. Cosine (cos x)
    10. Tangent (tan x)
    11. Log (base 10)
    12. Natural Log (ln)
    0. Exit
    """)

    choice = int(input("Enter your choice (0–12): "))

    # exit option
    if choice == 0:
        print("Goodbye!")
        break

    # Operations needing two numbers
    if choice in [1, 2, 3, 4, 5]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", num1 + num2)

        elif choice == 2:
            print("Result:", num1 - num2)

        elif choice == 3:
            print("Result:", num1 * num2)

        elif choice == 4:
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero!")

        elif choice == 5:
            print("Result:", math.pow(num1, num2))

    # Operations needing one number
    elif choice in [6, 7, 8, 9, 10, 11, 12]:
        num = float(input("Enter number: "))

        if choice == 6:
            if num >= 0:
                print("Result:", math.sqrt(num))
            else:
                print("Error: Square root of negative number not allowed")

        elif choice == 7:
            print("Result:", num ** 2)

        elif choice == 8:
            print("Result:", math.sin(math.radians(num)))

        elif choice == 9:
            print("Result:", math.cos(math.radians(num)))

        elif choice == 10:
            print("Result:", math.tan(math.radians(num)))

        elif choice == 11:
            if num > 0:
                print("Result:", math.log10(num))
            else:
                print("Error: Log defined only for positive numbers")

        elif choice == 12:
            if num > 0:
                print("Result:", math.log(num))
            else:
                print("Error: Natural log defined only for positive numbers")

    else:
        print("Invalid choice — try again!")