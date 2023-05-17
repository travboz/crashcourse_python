from pathlib import Path
import json

path = Path("favourite_number.json")
favNum = int(input("What is your favourite number? "))
contents = json.dumps(favNum)
path.write_text(contents)
