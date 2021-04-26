'''Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance'''


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")


class Restaurant:
    restaurant_1 = Restaurant('Hotel California', 'Continental')
    restaurant_1.describe_restaurant()

    restaurant_2 = Restaurant('Hotel Kass', 'Indian')
    restaurant_2.describe_restaurant()

    restaurant_3 = Restaurant('King Kong', 'Chinese')
    restaurant_3.describe_restaurant()
    