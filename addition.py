# Exercises 10-6 and 10-7 of Python Crash Course

# try:
#     print("Let's add two numbers.")
#     num1 = int(input("Enter number 1: "))
#     num2 = int(input("Enter number 2: "))

#     print(f"The result of {num1} + {num2} is {num1 + num2}.")

# except ValueError:
#     print("Cannot add those two values together.")


while True:
    """Create an addition prompt that results in addition of the two numbers provided."""
    try:
        print("Let's add two numbers.")
        print("To exit, type 'q' at any time.")
        num1 = input("Enter number 1: ")

        if num1.lower() == 'q':
            break
        num2 = input("Enter number 2: ")
        if num2.lower() == 'q':
            break

        print(f"The result of {num1} + {num2} is {int(num1) + int(num2)}.")

    except ValueError:
        print("Cannot add those two values together.")