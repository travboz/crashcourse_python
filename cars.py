def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a user."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

