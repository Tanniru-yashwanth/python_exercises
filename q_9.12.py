'''Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.'''


from priviliges_admin_module import Privileges, Admin


admin = Admin('Yashwanth', 'Tanniru', 23, 'Male')
admin.describe_user()
admin.privileges.show_privileges()