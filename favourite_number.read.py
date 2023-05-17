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

path = Path("favourite_number.json")
num = get_stored_number(path)

print(f"I know your favourite number! It's {num}.")