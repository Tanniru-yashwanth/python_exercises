class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"The Name of the user is {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}")

    def greet_user(self):
        print(f"Mr.{self.first_name} {self.last_name}, Welcome to the python world.")