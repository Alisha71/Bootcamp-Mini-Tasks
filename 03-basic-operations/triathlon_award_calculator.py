# Read the time (in minutes) for swimming, cycling and running
# Define the qualifying time in minutes 
qualifying_time = 100 

# Read the time taken for each event from the user
swimming_time = float(input("Enter the time taken for swimming (in minutes): "))
cycling_time = float(input("Enter the time taken for cycling (in minutes): "))
running_time = float(input("Enter the time taken for running (in minutes): "))

# Calculate the total time taken for the triathlon 
total_time = swimming_time + cycling_time + running_time

# Display the total time taken 
print(f"\nTotal time taken: {total_time:.2f} minutes")

# Determine the award based on the total time
if total_time <= qualifying_time:
    award = "Provincial Colours"
elif total_time <= qualifying_time + 5:
    award = "Provincial Half Colours"
elif total_time <= qualifying_time + 10: 
    award = "Provincial Scroll"
else: 
    award = "No award"

# Display the award
print(f"Award: {award}")
