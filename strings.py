# Using strings and various ways to work with strings

# using format() method
# person = input("What is your name?") # input function prompts the user to enter their name.
# message = "My name is {}".format(person) # format method is used to insert the value stored in the person variable into the placeholder {} within this string. The {} serves as a placeholder for substituting the values passed to the format() function.

# print(message)

# Output:
# My name is {your name goes here}

# END

# using format() method, with numbered placeholders {0}, {1}, {2} etc., to specify the order in which values should be inserted or reused.
# name = "Oladimeji"
# age = 30
# exp = 10
# message = "My name is {0}. I am {1} years old and I have {2} years of experience in data.".format(name, age, exp)

# print(message)

# END

# Working with multi-line strings with len function
# note_to_self = """I am a very passionate and focused individual 
# when my back is up against the wall, interesting."""

# print(note_to_self)
# print(len(note_to_self))

# END

# Using endswith() string method
# file_name_1 = "quaterly_report.pdf" # Could be file name or file path within the string to verify file formats before processing financial reports.

# if file_name_1.endswith(".pdf"): # Checks if the string ends with the specified suffix.
#     print("This file is a pdf document.")

# Using endswith() string method with a function with default parameters
def validate_file_format(file_name, required_format = ".pdf"): # use of parameters with default values makes your functions more flexible and reusable with other file types other than just the specified pdf files. See the 4 examples below...
    if file_name.endswith(required_format):
        return "Valid Format."
    else:
        return "Invalid Format."
    
report_filename = "accounting.pdf"
validate_report = validate_file_format(report_filename, ".pdf")
print(validate_report)
# Output: Valid Format.
    
result_pdf = validate_file_format("banking.pdf", ".pdf")
print(result_pdf)
# Output: Valid Format.
    
result_csv = validate_file_format("sales.csv", ".csv")
print(result_csv)
# Output: Valid Format.

result_docs = validate_file_format("transaction.docs", ".docs")
print(result_docs)
# Output: Valid Format.

# Using endswith() string method with a function alongside multiple conditions using if/elif/else statements - This example shows how the .endswith() method can play a crucial role in ensuring data integrity, security, and efficient processing.
def process_file_based_on_type(filename):
    if filename.endswith(".pdf"):
        return "Load to transaction database."
    elif filename.endswith(".csv"):
        return "Load to wise bank data exchange."
    elif filename.endswith(".docs"):
        return "Integrate with internal API"
    else:
        return "Invalid file format."

# File received from a data feed
data_feed_file = "daily_transactions.csv"
process_data = process_file_based_on_type(data_feed_file)
print(process_data)  # Output: "Load to wise bank data exchange."