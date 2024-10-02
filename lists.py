# A list is used to store multiple values in Python

# # Using a list to store names of my friends
# friends = ["Dave", "Peter", "Dan", "Joe", "moh", "femi"]
# print(friends)

# # Print out the type of friends - what data type is the friends list?
# print(type(friends))

# # Print out the friend, with the name starting with J
# print(friends[3])

# # Print out the first 2 element in the list using slicing and dicing method and store in new variable
# slicing_names = friends[:2]
# print(slicing_names)

# # Print out the last 4 element in the list using slicing and dicing method and store in new variable
# dicing_names = friends[-4:]
# print(dicing_names)

#END

# # A list of ages
# people_ages = [40, 10, 11.5, 28, 34, 69]

# #Create a copy of the list above using list constructor and save in new variable
# copy_people_ages = list(people_ages)

# #Create a copy of the list above using the copy method and save in new variable
# copy_people_ages1 = people_ages.copy()

# # Reassign an element in the original list, without changing the original people_ages list
# copy_people_ages[1] = 20

# copy_people_ages1[2] = 21

# print(copy_people_ages) # Replaces the index one which is 10, with 20.
# print(people_ages) # original
# print(copy_people_ages1) # Replaces the index two which is 11.5, with 21.

#END

# list with the slice operator[:] and append method
a = [1, 2, 3]
b = a[:] # creates new list that is a copy of a, but doesn't change the original list
a.append(4) # original list as now been changed to [1, 2, 3, 4] because of the .append() method

# if 4 in a:
#     print("4 is in list a.") # Output: 4 is in list a.

# print(a) # Output: [1, 2, 3, 4]
# print(b) # Output: [1, 2, 3]

# END

# List Comprehension

# Create a List of Square Roots - Write a list comprehension to create a list of square roots for all numbers from 1 to 10
# import math
# square_root = [math.sqrt(i) for i in range(1, 11)]
# print(square_root)
# Output: [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]

# Filter Out Positive Numbers - Given a list of numbers, use list comprehension to create a new list that contains only the positive numbers from the original list.
numbers = [-10, -5, 0, 5, 10, 15]

positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)
# Output: [5, 10, 15]