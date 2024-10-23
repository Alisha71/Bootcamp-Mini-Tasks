# Request user to enter a sentence
str_mandip = input("Please enter a sentence:")

# Calculate and display the length of the sentence 
length = len(str_mandip)
print(f"The length of the sentence is {length}")

# Find the last letter in the sentence 
last_letter = str_mandip[-1]

# Replace every occurence of the last letter of str_mandip with '@' 
str_replaced = str_mandip.replace(last_letter, "@")
print(f"The sentence after replacing '{last_letter}' with '@': {str_replaced}") 

# Print the last three characters in reverse
last_three_reversed = str_mandip[-3:][::-1]
print(f"The last three characters in reverse are: {last_three_reversed}")

# Create a 5-lettered word made up of the first 3 and last 2 characters
five_letter_word = str_mandip[:3] + str_mandip[-2:]
print(f"The new 5-letted workd is: {five_letter_word}")

