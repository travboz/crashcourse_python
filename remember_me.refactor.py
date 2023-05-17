from pathlib import Path
import json

# username = input("What is your name? ")
# path = Path("username.json")
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We'll remember you when you come back, {username}!")

def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remmeber you when you come back, {username}!")

greet_user()