from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for a new username."""
    user_info = {}
    user_info['username'] = input("What is your username? ")
    user_info['first_name'] = input("What is your first name? ")
    user_info['age'] = int(input("What is your age? "))

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    user_info = get_stored_user_info(path)
    if user_info:
        response = input(f"Are you {user_info['username']}? (y/n) ")
        if response.lower() == 'n' or response.lower() == 'no':
            user_info = get_new_user_info(path)
            print(f"We'll remember you when you come back, {user_info['first_name']}!")
        else:
            print(f"Welcome back, {user_info['username']}!")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['first_name']}!")

greet_user()