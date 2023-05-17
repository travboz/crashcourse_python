favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favourite languages are:")
    else:
        print(f"\n{name.title()}'s favourite language is:")
    # printing each language
    for language in languages:
        print(f"\t{language.title()}")