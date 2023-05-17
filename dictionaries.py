alien_0 = {'color': 'green', 'points': 5}

alien_1 = {}
print(alien_1)

alien_1 = {'color': 'orange', 'points': 10}
print(alien_1)

alien_1['color'] = 'teal'
print(alien_1)

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'fast', 'points': 10}
print(f"Original position is: {alien_2['x_position']}")

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}")

del alien_2['points']
print(alien_2)


favorite_languages = {
    'jen': 'python',
    'travis': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['travis'].title()
print(f"Travis' favourite language is {language}.")

favourite_lang = favorite_languages.get("nigel", "person isn't in our list")
print(favourite_lang)


glossary = {
    'loops': 'a way to iterate over items',
    'ifs': 'a method of allowing decisions to be made',
    'lists': 'when you want to store more than one value in a variable',
    'dictionaries': 'the structure used to store similar data',
    'slicing': 'for when you only want a bit of that pie'
}

print(f"Loops:         {glossary['loops']}")
print(f"If statements: {glossary['ifs']}")
print(f"Lists:         {glossary['lists']}")
print(f"Dictionaries:  {glossary['dictionaries']}")
print(f"Slicing:       {glossary['slicing']}")