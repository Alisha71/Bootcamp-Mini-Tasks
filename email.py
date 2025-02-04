# References:
# 1) Python Documentation (Official) https://docs.python.org/3/
# 2) Real Python: Object-Oriented Programming in Python  https://realpython.com/python3-object-oriented-programming/
# 3) Programiz: input() in Python https://www.programiz.com/python-programming/methods/built-in/input
# 4) GeeksforGeeks - Python Data Structures https://www.geeksforgeeks.org/python-data-structures-and-algorithms/
# 5) Head First Python: A Brain-Friendly Guide https://www.oreilly.com/library/view/head-first-python/9781491919521/

class Email:
    def __init__(self, sender_email, subject, content):
        """
        Initiate a fresh Email object equipped with these details.
        Args:
            sender_email (str): Email of the person sending it.
            subject (str): What the email is about: Subject Line
            content (str): What's in the email.
        """
        self.sender_email = sender_email
        self.subject = subject
        self.content = content
        self.has_been_read = False

    def mark_as_read(self):
        """
        Change the read status to confirm it's been looked at.
        """
        self.has_been_read = True

# Start by creating a blank list named "inbox" that will store email objects 
inbox = []

# Method on how to fill the user's inbox with sample emails
def populate_inbox():
    """
    Fills up the inbox with some Email objects that has been decided on.
    """
    inbox.append(Email("alisha.shah71@hotmail.com", "Welcome to Shiz University!", "Stoked to have you, whether you wanna become a sorcerer or witch!"))
    inbox.append(Email("rockalisha@hotmail.co.uk", "Just a head's up: please hand in your first mission from your wizard guide", "Make sure you turn it in by Monday, okay?"))
    inbox.append(Email("alisha.shah0xx@gmail.com", "Congrats!", "You made it into the Wizard program, awesome!"))

# Method to show every email
def list_emails():
    """
    This displays each email in the inbox, plus their number and whether they are new or seen.
    """
    if not inbox:
        print("\nYour inbox has zero emails.")
    else:
        print("\nCheck out these emails in your Inbox:")
        for i, email in enumerate(inbox):
            status = "(Read)" if email.has_been_read else "(Unread)" 
            print(f"{i} - {email.subject} {status}")

# Method to read a specific email
def read_email(index):
    """
    Reads and shows the email at the given index. 

    Args:
        index (int): The index of the email to read.
    """
    if not inbox:
        print("\nYour inbox is empty.")
        return

    try:
        email = inbox[index]
        print(f"\nFrom: {email.sender_email}")
        print(f"Subject: {email.subject}")
        print(f"Content: {email.content}\n")
        email.mark_as_read()
        print(f"\nEmail from {email.sender_email} marked as read.\n")
    except IndexError:
        print("\nInvalid index. Please select a valid email number.")
    except ValueError:
        print("\nPlease enter a number for the email index.")

# Method to show all unread emails
def view_unread_emails():
    """
    Shows all emails that users have not marked as read yet. 
    """
    unread_emails = [(i, email) for i, email in enumerate(inbox) if not email.has_been_read]
    if not unread_emails:
        print("\nYou have no unread emails.")
    else:
        print("\nHere are your unread emails:")
        for i, email in unread_emails:
            print(f"{i} - {email.subject}")

# Interactive menu function
def run_menu():
    populate_inbox()  # Populate the inbox with sample emails

    while True:
        # Display the menu
        print("\nMenu:")
        print("1. See a list of all emails")
        print("2. Read an email")
        print("3. Check out unread emails")
        print("4. Quit")

        user_choice = input("\nEnter your choice: ")  # Wait for actual user input

        if user_choice == "1":
            list_emails()
        elif user_choice == "2":
            try:
                index = int(input("\nWhich email do you want to open (enter email number)?: "))
                read_email(index)
            except ValueError:
                print("\nOops! Please enter a valid email number.")
        elif user_choice == "3":
            view_unread_emails()
        elif user_choice == "4":
            print("\nThanks for using the email menu. Goodbye!")
            break
        else:
            print("\nSorry, that is not an option, please try again.")

# Run the program
if __name__ == "__main__":
    run_menu()
