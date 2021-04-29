""" Modify your function so it requires a third parameter,
population. It should now return a single string of the form City, Country –
population xxx, such as Santiago, Chile – population 5000000. Run test
_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run test
_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that verifies
 you can call your function with the values 'santiago', 'chile', and
'population=5000000'. Run test_cities.py again, and make sure this new test
passes"""


import unittest
from city_functions import city_country_population


class CityCountryPopulation(unittest.TestCase):
    def test_city_country(self):
        city_country_population_ = city_country_population('Hyderabad', 'India', 5000000000)
        self.assertEqual(city_country_population_, 'Hyderabad, India 5000000000')


if __name__ == '__main__':
    unittest.main()


