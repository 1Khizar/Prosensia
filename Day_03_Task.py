# Python Internship – Day 3

# Taking a sentence input from the user
sentence = input("Enter a sentence: ")

# Splitting the sentence into a list of words
words_list = sentence.split()

print("List of words:", words_list)

# Joining the list back into a sentence 
join_sentence = ' - '.join(words_list)
print("Joined sentence with '-' separator:", join_sentence)

# Storing first and last name in a tuple
name_tuple = ("Khizar", "Ishtiaq")

# Printing each part of the tuple using indexing
print("First Name:", name_tuple[0])
print("Last Name:", name_tuple[1])
