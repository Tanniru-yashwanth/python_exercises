def make_car(manufacturer, model, **other_features):
    other_features['manufacturer_name'] = manufacturer
    other_features['model_name'] = model
    return other_features


car = make_car('skoda', 'rapid', colour='white', type='automatic')
print(car)