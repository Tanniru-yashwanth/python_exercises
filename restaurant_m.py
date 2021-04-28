

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, customers):
        self.number_served = customers
        print(f"The number of customers served: {self.number_served} ")

    def increment_number_served(self, customers_incremented):
        self.number_served += customers_incremented
        print(f"The number of customers served: {self.number_served} ")
