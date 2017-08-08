#!/usr/local/bin/python3
"""
wardrobe_03.py
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


class Shirt(Clothing):
    """Shirt subclass. Extends Clothing functionality"""

    def __init__(self, name, clean=True, times_worn=0, max_wears=1, \
                 short_sleeves=True):
        super().__init__(name, clean, times_worn, max_wears)
        self.short_sleeves = short_sleeves

    def has_short_sleeves(self):
        """return True if a shortsleeved shirt"""
        return self.short_sleeves

    def __str__(self):
        """extending Clothing.__str__ method"""
        return  "Shirt[" + super().__str__() + \
                ", short_sleeves=" + str(self.short_sleeves) + \
                "]"



def main():
    """The main function will test the Clothing class"""
    my_clothes = []
    my_clothes.append(Clothing("blue jeans", True))
    my_clothes.append(Clothing("baseball cap", True, 20, 1000))
    my_clothes.append(Clothing("jacket", True, 20, 100))
    my_clothes.append(Shirt("t-shirt", True, 0, 1, True))
    my_clothes.append(Shirt("dress shirt", True, 0, 1, False))

    def wear_item(item):
        """call wear method on named item variable"""
        for i, _ in enumerate(my_clothes):
            if my_clothes[i].get_name() == item:
                my_clothes[i].wear()

    wear_item('t-shirt')
    wear_item('blue jeans')

    print("\n==== Full Wardrobe ==========")
    for i, _ in enumerate(my_clothes):
        print(my_clothes[i])

    print("\n==== Clean clothes ==========")
    for i, _ in enumerate(my_clothes):
        if my_clothes[i].is_clean():
            print(my_clothes[i])

    print("\n==== Dirty clothes ==========")
    for i, _ in enumerate(my_clothes):
        if not my_clothes[i].is_clean():
            print(my_clothes[i])

    print("\n==== All Shirts =============")
    for i, _ in enumerate(my_clothes):
        if isinstance(my_clothes[i], Shirt):
            print(my_clothes[i])

    print("\n==== Clean Shirts ===========")
    for i, _ in enumerate(my_clothes):
        if isinstance(my_clothes[i], Shirt):
            if my_clothes[i].is_clean():
                print(my_clothes[i])

    print("\n==== Dirty Shirts ===========")
    for i, _ in enumerate(my_clothes):
        if isinstance(my_clothes[i], Shirt):
            if not my_clothes[i].is_clean():
                print(my_clothes[i])


if __name__ == "__main__":
    main()
