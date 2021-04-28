'''Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant.
Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working properly'''


from restaurant_m import Restaurant
restaurant = Restaurant('Paradise', 'Indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()


import restaurant_m
restaurant = restaurant_m.Restaurant('Paradise', 'Indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()


from restaurant_m import Restaurant as Rs
restaurant = Rs('Paradise', 'Indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()


from restaurant_m import*
restaurant = Restaurant('Paradise', 'Indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
