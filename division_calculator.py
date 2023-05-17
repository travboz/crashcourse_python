# Leads to a div by 0 error:
# print(5/0)

#### try-except
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# deeper example
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)