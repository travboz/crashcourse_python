from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # you don't need to always notify the user. you can fail silently.
        # using the keyword:
        pass
        # print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# path = Path('1984.txt')
# count_words(path)


filenames = ['1984.txt', 'moby_dick.txt', 'paul_blart_mallcop.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)


