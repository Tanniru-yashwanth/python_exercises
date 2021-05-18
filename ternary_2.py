"""Using ternary operator, write a program to check whether a person is eligible for voting or not."""

age = int(input("Enter the age: "))
result = "Eligible for voting" if age > 18 else "Not Eligible for voting"
print(result)
