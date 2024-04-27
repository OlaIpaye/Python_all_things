# # Basic arithmetic operations in Python
# a = 3
# b = 5.5
# c = "Ola"

# print(a + b)

# # Using the type() fucntion to find out the type of data type is stored in that variable.
# print(type(a)) # used the type function insdie the print command to output the code.
# print(type(b))
# print(type(c))

## End

# Operations with Other Types
monthly_income = 100
monthly_expence = 30.6
goals = "I don't have a goal yet!"
goals = "I want to save at least 60 out of my monthly income"
total_savings = "500.10"

# Using the above code Calculate the total monthly savings using monthly_income and monthly_expence and save it inside monthly_savings
monthly_savings = monthly_income - monthly_expence
print(monthly_savings) # Output: 69.4

# Using the above code, print the type of monthly_savings
print(type(monthly_savings))

# Print out the goals and type of goals
print(goals) # Output: the bottom goals variable since python reads from top to bottom and reassings its value.
print(type(goals))

# End

# Type Conversion

# Print out monthly_income and convert it into a str
print("The monthly income is " + str(monthly_income))

# Convert total_savings into a float and save it inside savings_float
savings_float = float(total_savings)
print(savings_float)
