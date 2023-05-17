prompt = "Please enter a number: "
number = int(input(prompt))

if number % 10 == 0:
    print(f"\n{number} is divisible by 10.")
else:
    print(f"\n{number} is not divisible by 10.")
