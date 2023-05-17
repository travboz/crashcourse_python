import random

favourite_places = {}

favourite_places = {
    'harold': ['bed', 'the zoo', 'schools'],
    'travis': ['bed', 'the loo', 'bunnings'],
    'nigel': ['the jungle', 'the zoo', 'in mud'],
    }

for friend, place in favourite_places.items():
    print(f"One of {friend.title()}'s favourite places is ")
    print(f"{place[random.randint(0,2)]}")
