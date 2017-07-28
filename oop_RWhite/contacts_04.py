#!/usr/local/bin/python3
"""contacts_02.py
This program allows me to manage my contacts.
@author George Kaimakis
@version 2017-07-28
"""

# This file was created on 28/07/2017
# Author: George Kaimakis - https://github.com/geokai

class Person(object):
    """The Person class defines a person in terms of a
    name, phone number and email address.
    """

    # Constructor (initialiser)
    def __init__(self, theName, thePhone, theEmail):
        """Instantiate an object of class Person"""
        self.name = theName
        self.phone = thePhone
        self.email = theEmail

    # Accessor Methods (getters)
    def get_name(self):
        """returns the name"""
        return self.name

    def get_phone(self):
        """returns the phone number"""
        return self.phone

    def get_email(self):
        """returns the email"""
        return self.email

    # Mutator Methods (setters)
    def set_phone(self, new_phone_number):
        """sets new phone number"""
        self.phone = new_phone_number

    def set_email(self, new_email_address):
        """sets new email address"""
        self.email = new_email_address

    def __str__(self):
        """This method overrides the superclass object.__str__() method"""
        return  "Person[name=" + self.name + \
                " ,phone=" + self.phone + \
                " ,email=" + self.email +\
                "]"


def enter_a_friend():
    """Create an entry for a friend (initialiser)"""
    name = input("Enter friend's name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    return Person(name, phone, email)

def lookup_a_friend(friends):
    """Search listing for an entry"""
    found = False
    name = input("Enter friend's name: ")
    for friend in friends:
        if name in friend.get_name():
            print(friend)
            found = True
    if not found:
        print("No friends match that term")

def show_all_friends(friends):
    """Print all listings"""
    print("Showing all contacts:")
    for friend in friends:
        print(friend)

def main():
    """Main function"""
    friends = []
    running = True

    while running:
        print("\nContacts Manager")
        print("1) new contacts    2) lookup")
        print("3) show all        4) exit ")
        option = input("> ")
        if option == "1":
            friends.append(enter_a_friend())
        elif option == "2":
            lookup_a_friend(friends)
        elif option == "3":
            show_all_friends(friends)
        elif option == "4":
            running = False
        else:
            print("Unrecognized input, Please try again.")
    print("Program exiting.")


#    print(dir(friend1))
#    print(dir(Person))


if __name__ == "__main__":
    main()
