'''An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method'''


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


class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = 'can add post', 'can delete post', 'can ban user'

    def show_privileges(self):
        print(f"The privileges of Administration are : {self.privileges}")


admin = Admin('Yashwanth', 'Tanniru', 23, 'Male')
admin.greet_user()
admin.show_privileges()