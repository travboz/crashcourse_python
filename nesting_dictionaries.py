alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'orange', 'points': 15}
alien_2 = {'colour': 'gray', 'points': 10}

# a list of dictionaries
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# more realistic example
aliens = []

# make 30 green aliens
for alien_count in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# printing first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print(f"Current strength of our Alien Armada: {len(aliens)}!")


# modifying some of our aliens
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# showing our updated aliens
for alien in aliens[:6]:
    print(alien)
print("...")

for alien in aliens[27:]:
    if alien['colour'] == 'green':
        alien['colour'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[27:]:
    print(alien)


# lists in dictionaries

pizza = {
    'crust': 'cheesy',
    'toppings': ['pepperoni', 'extra cheese', 'mushrooms', 'bacon', 'capsicum'],
    }

# summarise the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

print("... to eat while the world ends.")