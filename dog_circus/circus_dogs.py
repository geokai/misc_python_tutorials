"""Circus dogs class module"""

# This file was created on 04/08/2017
# Author: George Kaimakis - https://github.com/geokai


class CircusDogs(object):
    """Create circus dog class objects"""

    def __init__(self, name, breed):
        """create instance with name, breed and trick-list"""
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

    def num_tricks(self):
        """return the number of tricks"""
        for num, _ in enumerate(self.tricks, 1):
            pass
        return num
