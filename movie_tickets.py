prompt = "\nMovie prices are age-dependant."
prompt += "\n(Enter 'quit' when you are finished.) \n"
print(prompt)

prompt = "\nPlease enter your age: "

while True:
    age = input(prompt)
    if age.lower() == "quit":
        break
    age = int(age)
    print("The ticket is ")
    if age < 3:
        print("free.")
    elif age >= 3 and age < 12:
        print("$10.")
    else:
        print("$15.")

