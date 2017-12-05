"""
contacts03.py
This program allows me to manage my contacts.
"""


class Person(object):
    """
    The Person class defines a person in terms of a
    name, phone number, and email address.
    """

    # Constructor
    def __init__(self, theName, thePhone, theEmail):
        self.name = theName
        self.phone = thePhone
        self.email = theEmail

    # Accessor Methods (getters)
    def get_name(self):
        """Returns instance name"""
        return self.name

    def get_phone(self):
        """Returns instance phone"""
        return self.phone

    def get_email(self):
        """Returns instance email"""
        return self.email

    # Mutator Methods (setters)
    def set_phone(self, newPhoneNumber):
        """resets the instance phone variable"""
        self.phone = newPhoneNumber

    def set_email(self, newEmailAddress):
        """resets the instance email"""
        self.email = newEmailAddress

    def __str__(self):
        return  "Person[name: " + self.name + \
                ", phone: " + self.phone + \
                ", email: " + self.email + \
                "]"


def main():

    friend1 = Person("Jill", "123-4567", "jbush@gmail.org")
    print(friend1.get_email())
    friend1.set_email("jbush@gmail.com")
    print(friend1.get_email())
    print(friend1)

if __name__ == "__main__":
    main()
