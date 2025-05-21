# Request the user to enter their full name 
full_name = input("please enter your full name: ")

# Validate user input
if len(full_name.strip()) == 0:
    print("You haven't entered anything. Please enter your full name. ")

elif len(full_name.strip()) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

elif len(full_name.strip()) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

else:
    print("Thank you for entering your name.")
