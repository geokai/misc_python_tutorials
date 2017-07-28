#!/usr/local/bin/python3
"""contacts_02.py
This program allows me to manage my contacts.
@author George Kaimakis
@version 2017-07-28
"""

# This file was created on 28/07/2017
# Author: George Kaimakis - https://github.com/geokai

def main():
    """Main function"""

    friends = []

    for i in range(2):
        print("Contact manager")
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        friends.append([name, phone, email])

    for i in range(len(friends)):
        print("Contact Info")
        for j in range(len(friends[i])):
            print(friends[i][j])


if __name__ == "__main__":
    main()
