# Using strings and various ways to work with strings

# using format() method
# person = input("What is your name?") # input function prompts the user to enter their name.
# message = "My name is {}".format(person) # format method is used to insert the value stored in the person variable into the placeholder {} within this string. The {} serves as a placeholder for substituting the values passed to the format() function.

# print(message)

# Output:
# My name is {your name goes here}

# END

# using format() method, using numbered placeholders {0}, {1}, {2} etc., to specify the order in which values should be inserted or reused.
# name = "Oladimeji"
# age = 30
# exp = 10
# message = "My name is {0}. I am {1} years old and I have {2} years of experience in data.".format(name, age, exp)

# print(message)

# END

# Working with multi-line strings with len function
note_to_self = """I am a very passionate and focused individual 
when my back is up against the wall, interesting."""

print(note_to_self)
print(len(note_to_self))