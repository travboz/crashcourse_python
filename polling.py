favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

should_poll = ['john', 'carter', 'emile', 'phil', 'jen']

for person in should_poll:
    if person in favorite_languages.keys():
        print(f"Thank you {person} for already participating in this poll.")
    else:
        print(f"Thank you new participant for your first poll vote!")