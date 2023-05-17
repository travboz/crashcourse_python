class Dog:
    """A simple dog model."""
    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")



harold = Dog('Harold', 6)
print(f"There is this one dog named {harold.name}.")
print(f"Harold hasn't been around for too long, {harold.age} years to be exact.")

harold.sit()
harold.roll_over()