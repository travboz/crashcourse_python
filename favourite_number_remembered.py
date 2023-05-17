from pathlib import Path
import json

def get_stored_number(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        num = json.loads(contents)
        return num
    else:
        return None


def get_new_favNum(path):
    """Prompt for a new favourite number."""
    favNum = int(input("What is your favourite number? "))
    contents = json.dumps(favNum)
    path.write_text(contents)

    return favNum


def get_fav_num():
    """Get the user's favourite number."""
    path = Path("favourite_number.json")
    favNum = get_stored_number(path)
    if favNum:
        print(f"I know your favourite number! It's {favNum}!")
    else:
        favNum = get_new_favNum(path)

get_fav_num()