'''An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method'''


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_name):
        super().__init__(restaurant_name, cuisine_name)
        self.flavours = 'vanilla', 'strawberry', 'chocolate'

    def display_flavours(self):
        print(f"The flavours of ice_cream are {self.flavours}")


ice_cream_stand = IceCreamStand('Ice_cream_stand', 'ice_cream_parlour')
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavours()
