from city_functions import city_and_country

def test_city_country():
    city_country = city_and_country('santiago', 'chile', 5_000_000)
    assert city_country == 'Santiago, Chile - population 5000000'