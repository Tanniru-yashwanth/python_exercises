'''Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user'''


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


class User:
    user = User('Yashwanth', 'Tanniru', 23, 'Male')
    user.describe_user()
    user.greet_user()
