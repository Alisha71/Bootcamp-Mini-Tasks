# Request user to enter their favourite restaurant 
string_fav = input("Please enter the name of your favourite restaurant:")

# Request user to enter their favourite number 
int_fav = int(input("Please enter your favourite number:"))

# Print both values on seperate lines 
print(f"Your favourite restaurant: {string_fav}")
print(f"Your favourite number: {int_fav}")

# Try to cast string_fav to an integer (will raise an error)
cast_value = int(string_fav)
print(f"Casted value of restaurant name to integer: {casted_value}")

print("Error: You cannot cast a string like a restaurant name to an integer.")

# Comments why string_fav cannot be casted to an int: 
# There are errors because string_fav contains characters (letters)
# that cannot be interpreted as numbers.
# Only strings with numeric values can be cast to integers. 