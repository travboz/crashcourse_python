class Restaurant:
    """A model of a Restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This restuarant is named {self.restaurant_name}, and focuses on a cuisine style of {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name}, is now open.")

luigis = Restaurant("Luigi's Pasta", "Pasta")

print(luigis.restaurant_name)
print(luigis.cuisine_type)

luigis.describe_restaurant()
luigis.open_restaurant()

marios = Restaurant("Mario's Pizzeria", "Pizza")

print(marios.restaurant_name)
print(marios.cuisine_type)

marios.describe_restaurant()
marios.open_restaurant()

franks = Restaurant("Frank's BBQ", "Texas BBQ")

print(franks.restaurant_name)
print(franks.cuisine_type)

franks.describe_restaurant()
franks.open_restaurant()