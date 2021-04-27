''' Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''


class User:
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"The Name of the user is {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}")

    def greet_user(self):
        print(f"Mr.{self.first_name} {self.last_name}, Welcome to the python world.")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"The login attempts were incremented to {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"The login attempts reset to {self.login_attempts}")


class User:
    user = User('Yashwanth', 'Tanniru', 23, 'Male', 2)
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.reset_login_attempts()
