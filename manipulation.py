# Request user to enter a sentence
sentence = input("Please enter a sentence:")

# Calculate and display the length of the sentence 
length = len(sentence)
print(f"The length of the sentence is {length}")

# Find the last letter in the sentence 
last_letter = sentence[-1]

# Replace every occurrence of the last letter of sentence with '@' 
modified_sentence = sentence.replace(last_letter, "@")
print(f"The sentence after replacing '{last_letter}' with '@': {modified_sentence}") 

# Print the last three characters in reverse
last_three_reversed = sentence[-3:][::-1]
print(f"The last three characters in reverse are: {last_three_reversed}")

# Create a 5-lettered word made up of the first 3 and last 2 characters
five_letter_word = sentence[:3] + sentence[-2:]
print(f"The new 5-lettered word is: {five_letter_word}")


