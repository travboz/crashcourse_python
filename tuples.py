dimensions = (200, 50)
print(dimensions)

for dim in dimensions:
    print(dim)

# in order to define a tuple, it needs a comma
# if we have my_typle = (3), this is identical to my_typle = 3
my_typle = (3,)
# this way, my_typle is a single sized tuple
print(my_typle)

print(dimensions[0])

# cannot modify a tuple
# dimensions[0] = 100
# we must redefine the entire typle
dimensions = (100, 10000)
print(dimensions)



# tuple exercise: Buffet
print("Current buffet items:")
buffet_foods = ("prawns", "oysters", "crab", "mussels", "salmon")
for food in buffet_foods:
    print(food)

# does not work
# buffet_foods[1] = "langoustine"
# works
buffet_foods = ("prawns", "langoustine", "crab", "mussels", "salmon", "balmain bug")
print("Updated buffet items:")
for food in buffet_foods:
    print(food)
