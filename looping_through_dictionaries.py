user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("----------------------------------")
# looping over keys in dictionary
for name in favorite_languages.keys():
    print(name.title())

print("----------------------------------")

# looping over values; doesn't worry about duplicates
for language in favorite_languages.values():
    print(language.title())

print("----------------------------------")

# looping over sorted keys
for name in sorted(favorite_languages.keys()):
    print(name.title())

print("----------------------------------")

# looping over values; no duplicates
for language in set(favorite_languages.values()):
    print(language.title())


# set notation
languages = {'python', 'c', 'rust', 'java', 'python', 'c'}
print(languages)