prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) \n"

while True:
    city = input(prompt)

    if city.lower() == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")