# A list is used to store multiple values in Python

# Using a list to store names of my friends
friends = ["Dave", "Peter", "Dan", "Joe", "moh", "femi"]
print(friends)

# Print out the type of friends - what data type is the friends list?
print(type(friends))

# Print out the friend, with the name starting with J
print(friends[3])

# Print out the first 2 element in the list using slicing and dicing method and store in new variable
slicing_names = friends[:2]
print(slicing_names)

# Print out the last 4 element in the list using slicing and dicing method and store in new variable
dicing_names = friends[-4:]
print(dicing_names)