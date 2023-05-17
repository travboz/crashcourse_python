from pathlib import Path

cat_path = Path("cats.txt")
dog_path = Path("horses.txt")


try:
    cat_contents = cat_path.read_text(encoding='utf-8')
    dog_contents = dog_path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass
    # print(f"Sorry, a file does not exist.")
else:
    # Count the approximate number of words in the file:
    print(cat_contents)
    print("------------------")
    print(dog_contents)