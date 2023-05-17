from pathlib import Path

paths = ["1984.txt", "moby_dick.txt"]

for p in paths:
    path = Path(p)

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the exact number of 'the's in the file:
        print(f"The word 'the' appears {contents.lower().count('the')} times in {p.title()}")