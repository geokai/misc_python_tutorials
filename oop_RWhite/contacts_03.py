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


def main():
    """Main function"""

    friend1 = Person('Meg', '555-1234', 'meg@mail.org')
    print()
    print(friend1.get_email())
    friend1.set_email('meg@mail.com')
    print(friend1.get_email())
    print(friend1)
    print()

#    print(dir(friend1))
#    print(dir(Person))


if __name__ == "__main__":
    main()
