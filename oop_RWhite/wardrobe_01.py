#!/usr/local/bin/python3
"""
wardrobe_01.py
A class that keeps a track of my wardrobe state
@author George Kaimkais
@version 2017-07-29
"""


class Clothing(object):
    """ The Clothing class defines a piece of clothing in terms of
    its name and its cleanliness.
    """

    def __init__(self, name, clean=True):
        """Initialize an object with name & whether clean or not"""
        self.name = name
        self.clean = clean

    def get_name(self):
        """returns name of object"""
        return self.name

    def is_clean(self):
        """returns boolean of var clean"""
        return self.clean

    def __str__(self):
        """overriding 'object' superclass method"""
        return  "Clothing[name = " + self.name + \
                ", clean = " + str(self.clean) + \
                "]"


def main():
    """The main function will test the Clothing class"""
    my_jeans = Clothing("blue jeans", False)
    my_shorts = Clothing("shorts")
    print(my_jeans.get_name())
    print(my_shorts.is_clean())
    print(my_jeans)

if __name__ == "__main__":
    main()
