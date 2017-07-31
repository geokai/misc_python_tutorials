#!/usr/local/bin/python3
"""
wardrobe_02.py
A class that keeps a track of my wardrobe state
@author George Kaimkais
@version 2017-07-29
"""


class Clothing(object):
    """ The Clothing class defines a piece of clothing in terms of
    its name and its cleanliness.
    """

    def __init__(self, name, clean=True, times_worn=0, max_wears=1):
        """Initialize an object with name & whether clean or not"""
        self.name = name
        self.clean = clean
        self.times_worn = times_worn
        self.max_wears = max_wears

    def get_name(self):
        """returns name of object"""
        return self.name

    def is_clean(self):
        """returns boolean of var clean"""
        return self.clean

    def wear(self):
        """tracks the number of times worn and clean state"""
        self.times_worn += 1
        if self.times_worn >= self.max_wears:
            self.clean = False

    def wash(self):
        """resets clean & times_worn"""
        self.clean = True
        self.times_worn = 0

    def __str__(self):
        """overriding 'object' superclass method"""
        return  "Clothing[name=" + self.name + \
                ", clean=" + str(self.clean) + \
                ", times_worn=" + str(self.times_worn) + \
                ", max_wears=" + str(self.max_wears) + \
                "]"


def main():
    """The main function will test the Clothing class"""
    my_jeans = Clothing("blue jeans", False)
    my_jeans.wear()
    print(my_jeans)
    my_jeans.wash()
    print(my_jeans)

if __name__ == "__main__":
    main()
