from random import choice
from random import randint

# numbers = [randint(1, 26) for i in range(10)]
# letters = ['a', 'h', 'd', 't', 'm']

options = [randint(1, 26) for i in range(10)] + ['a', 'h', 'd', 't', 'm']

# print(options)
my_picks = [2, 20, 't', 'a']
winning_numbers = [choice(options) for i in range(4)]

count = 0
while True:
    winning_numbers = [choice(options) for i in range(4)]
    # if my_picks == winning_numbers: # this takes tooooooooooo long
    print(winning_numbers)
    if 'a' in winning_numbers and 2 in winning_numbers: # this is better
        break
    count += 1
print(count)

