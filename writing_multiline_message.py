from pathlib import Path

path = Path("graphics_goal.txt")

contents = "I want to write a graphics engine.\n"
contents += "So I can learn how to use classes.\n"
contents += "And apply linear algebra to a cool project.\n"

path.write_text(contents)

