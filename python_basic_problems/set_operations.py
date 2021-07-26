# Python Program to Illustrate Different Set Operations

set1 = (input("Enter the first set elements:").split(" "))
set1 = set(set1)
set2 = (input("Enter the second set elements:").split(" "))
set2 = set(set2)
print("Press a for addition")
print("Press u for union")
print("Press i for intersection")
print("Press d for Difference")
print("Press s for SymmetricDifference")
operation = input("Enter the operation:")
if operation == 'u':
    print(set1.union(set2))
elif operation == 'i':
    print(set1.intersection(set2))
elif operation == 'd':
    print(set1.difference(set2))
elif operation == 's':
    print(set1.symmetric_difference(set2))
