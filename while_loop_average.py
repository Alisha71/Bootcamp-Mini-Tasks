# Initialise variables 
total = 0 
count = 0 

# Start the while loop 
while True:
    number = int(input("Enter a number (-1 to stop): "))

    # Check if the user entered -1
    if number == -1:
        break # Exit the loop if the user enters -1

    # Add the number to the total and increment the count
    total += number
    count += 1

# Check to avoid division by zero
if count > 0:
    average = total / count
    print(f"The average of the numbers entered is: {average}")
else:
    print("No numbers were entered.")