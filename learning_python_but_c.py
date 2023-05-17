from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

print(contents)

print("-----------------------")

lines = contents.splitlines()

for line in lines:
    print(line)


# now we modify it to say "In C you can..."

print("-----------------------")

for line in lines:
    print(line.replace("Python", "C"))
