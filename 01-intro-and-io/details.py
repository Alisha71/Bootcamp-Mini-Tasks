# request user to enter their name and store the input in the name variable.

# request user to enter their age and store the input in the age variable.

# request user to enter their house number and store the input in the house_number variable.

# request user to enter their street name and store the input in the stree_name variable. 

# write a sentence which includes the user's name, age, house number, and street name using the values stored in the variables. 

# display the sentence to the user. 


# request name from user 
name = input("Please enter your name:")

# request age from user 
age = int(input("Please enter your age:"))

# request house number from user
house_number = input("Please enter your house number:")

# request street number from user 
street_name = input("Please enter your street name:")

# print out all the collected details in a sentence using an f-string
print(f"This is {name}. They are {age} years old and live at house number {house_number} on {street_name}.")

