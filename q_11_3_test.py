
import unittest
from q_11_3 import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Yashwanth', 'Tanniru', '10000')

    def test_give_default_rise(self):
        self.employee.give_rise()
        self.assertEqual(self.employee.annual_salary, 15000)

    def test_give_custom_raise(self):
        self.employee.give_rise(10000)
        self.assertEqual(self.employee.annual_salary, 20000)


if __name__ == '__main__':
    unittest.main()

