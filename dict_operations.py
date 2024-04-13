# Working with Dictionary

# Task: count how many times each letter from the text variable appears in a string. The keys will be each letter, and the values will be the amount of times the letter appears in the string.

text = "the quick brush jumped over the lazy crab"

# Use a dictionary to keep track of the letters I have seen in the above variable. Starting with an empty dictionary.

letter_counts = {}

for letter in text: #Use a for loop to iterate over each letter in the string
    if letter not in letter_counts: #Check if each letter is already in the empty dictionary of letter counts above. I do this using the "not in" membership operation.
        letter_counts[letter] = 1 #If it is not, it will add it to the dictionary with a starting count of 1.
    else: #If it is, I will increment the count for each letter.
        letter_counts[letter] = letter_counts[letter] + 1
print(letter_counts) #Print out the output of the code to the terminal.