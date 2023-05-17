# *toppings represents an "arbitrary length" argument statement
# that, it could be one, none or ten thousand
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    for topping in toppings:
        print(f" - {topping}")

# make_pizza()
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# you can mix the arbitrary args and normal positional args
# eg:

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')