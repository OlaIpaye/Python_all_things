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

# End


# Write this function that counts the number of words by how many letters they have.

def count_words_by_length(words):
    word_length_frequency = {} #created an empty dictionary
    for word in words: #Use a for loop to iterate through every word in the function
        word_length = len(word) #Use the len function to get the length of every word and assign to new variable
        if word_length not in word_length_frequency: #Then if the word is not in the empty dictionary already, set it to 1 because there is a word with the length of 1 in the function.
            word_length_frequency[word_length] = 1
        else: #If it is, get the current value of the word and then add 1 to it and then set it to the current word length.
            word_length_frequency[word_length] = word_length_frequency[word_length] = 1
    print(word_length_frequency) #Print the output.


count_words_by_length(["hat", "cat", "I", "bird"])


# End