# Request the user to enter three different integers 
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
num3 = int(input("Enter your third number:"))

# Calculate the sum of all three numbers
sum_of_numbers = num1 + num2 + num3
print(f"The sum of all numbers is: {sum_of_numbers}")

# Calculate the first number minus the second number 
difference = num1 - num2 
print(f"The first number minus the second number is: {difference}")

# Calculate the third number multiplied by the first number
product = num3 * num1 
print(f"The third number mutiplied by the first number is: {product}")

# Calculate sum of all three numbers divided by the third number
if num3 != 0: # Ensure we do not divide by zero
   result = sum_of_numbers / num3
   print(f"The sum of all numbers divided by the third number is: {result}")

else: 
   print("Division of zero is not allowed.")

