motorbikes = ["yamaha", "aprilia", "triumph", "suzuki", "ktm", "bmw"]

for bike in motorbikes:
    print(bike)

print(motorbikes[1:2])
print(motorbikes[:3])
print(motorbikes[:])
print(motorbikes[1:])

for bike in motorbikes[2:]:
    print(bike.title())


# the correct way to copy
my_foods = ['pizza', 'chicken', 'carrot cake']
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)

my_foods.append('hamburger')
friend_foods.append('cheese')

print(my_foods)
print(friend_foods)

print("-----------------------------------")

# the incorrect way to copy a list
my_foods = friend_foods

print(my_foods)
print(friend_foods)

my_foods.append('hamburger')
friend_foods.append('cheese')

print(my_foods)
print(friend_foods)

print("-----------------------------------")
# printing the lists with a loop

my_foods = ['popcorn', 'steak', 'choc chip cookie']
friend_foods = my_foods[:]

my_foods.append('brisket')
friend_foods.append('escargot')

print("My foods:")
for food in my_foods:
    print(food)

print("My friend's foods:")
for food in friend_foods:
    print(food)