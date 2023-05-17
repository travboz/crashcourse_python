cities = {
    'sapporo': {
        'country': 'japan',
        'population': 2_000_000,
        'fact': 'it is the largest city on hokkaido',
    },
    'jakarta': {
        'country': 'indonesia',
        'population': 10_562_088,
        'fact': 'it is the economic, cultural, and political centre of the country',
    },
    'hyderabad': {
        'country': 'india',
        'population': 6_900_000,
        'fact': 'much of hyderabad is situated on hilly terrain around articial lakes',
    }
}

for city, city_info in cities.items():
        print(f"{city_info['country'].title()}" f" has an approximate population of {city_info['population']} and one fun fact "
              f"about {city_info['country'].title()} is {city_info['fact'].lower()}.\n")