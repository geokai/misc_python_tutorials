"""Circus dogs class module"""

# This file was created on 04/08/2017
# Author: George Kaimakis - https://github.com/geokai


class CircusDogs(object):
    """Create circus dog class objects"""

    def __init__(self, name, breed):
        """create instance with name, breed and empty trick-list"""
        self.name = name
        self.breed = breed
        self.tricks = []

    def get_name(self):
        """return name"""
        return self.name

    def get_breed(self):
        """return breed"""
        return self.breed

    def add_trick(self, trick):
        """add/append trick to tricks list"""
        self.tricks.append(trick)

    def get_tricks(self):
        """return list of tricks"""
        return self.tricks

    def num_of_tricks(self):
        """return the number of tricks"""
        for index, _ in enumerate(self.tricks, 1):
            pass
        return index


SAL_DOG = CircusDogs('Sally', 'Poodle')
KIP_DOG = CircusDogs('Kipper', 'Beagle')

print(SAL_DOG.get_name())
print(KIP_DOG.get_name())
