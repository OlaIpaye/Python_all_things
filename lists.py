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

# print(people_ages)
# print(copy_people_ages) # Replaces the 10 with 20.
# print(copy_people_ages1)

#END

# list with the slice operator[:] and append method
a = [1, 2, 3]
b = a[:] #new list that is a copy of a, but doesn't change the original list
a.append(4) # original list as now been changed to [1, 2, 3, 4] because of the .append method

print(a) # Output: [1, 2, 3, 4]
print(b) # Output: [1, 2, 3]