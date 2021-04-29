
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def display_name(self):
        print(f"{self.first_name}, {self.last_name}, {self.annual_salary}")

    def give_rise(self, added_income=5000):
        self.annual_salary += int(added_income)
        return self.annual_salary
