#!/usr/local/bin/python3
"""contacts_01.py
This program allows me to manage my contacts.
@author George Kaimakis
@version 2017-07-28
"""

# This file was created on 28/07/2017
# Author: George Kaimakis - https://github.com/geokai

def main():
    """Main function"""
    print("Contact manager")
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    print(name, phone, email)


if __name__ == "__main__":
    main()
