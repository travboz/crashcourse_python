from pathlib import Path

# printing one for one what's in the file
path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

# example of modifying the contents
path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

print("---------------------------------------")

# splitting the lines of a file into an array
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)