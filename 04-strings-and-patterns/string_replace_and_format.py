# Step 1: Write the single string with exclamation marks 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Step 2: Replace '!' with ' ' (space)
sentence_with_spaces = sentence.replace("!", " ")
print(sentence_with_spaces)

# Step 3: Convert the sentence to uppercase
uppercase_sentence = sentence_with_spaces.upper()
print(uppercase_sentence) 

# Step 4: Reverse the sentence 
reversed_sentence = sentence_with_spaces [::-1]
print(reversed_sentence)

