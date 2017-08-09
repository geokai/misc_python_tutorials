"""Circus dogs class module"""

# This file was created on 04/08/2017
# Author: George Kaimakis - https://github.com/geokai


class CircusDogs(object):
    """Create circus dog class objects"""

    circus_dogs = []
    num_of_dogs = 0

    def __init__(self, name, breed):
        """create instance with name, breed and empty trick-list"""
        self.name = name
        self.breed = breed
        self.tricks = []
        self.trick_counter = 0
        # increment number of instances created
        CircusDogs.num_of_dogs += 1
        # add created instances to list of dogs
        CircusDogs.circus_dogs.append(self.name)

    def get_name(self):
        """return name"""
        return self.name

    def get_breed(self):
        """return breed"""
        return self.breed

    def add_trick(self, trick):
        """add/append trick to tricks list & increment trick counter"""
        self.tricks.append(trick)
        self.num_of_tricks()

    def get_tricks(self):
        """return list of tricks"""
        return self.tricks

    def num_of_tricks(self):
        """return the number of tricks"""
        for index, _ in enumerate(self.tricks, 1):
            self.trick_counter = index
        return self.trick_counter

    def __str__(self):
        return "Circus Dog[name: " + self.name + \
                ", Breed: " + self.breed + \
                ", Tricks: " + str(self.tricks) + \
                ", Trick-count: " + str(self.trick_counter) + \
                "]"

SAL_DOG = CircusDogs('Sally', 'Poodle')
KIP_DOG = CircusDogs('Kipper', 'Beagle')
FR_DOG = CircusDogs('Frank', 'Pug')

CIRCUS_DOGS = []
CIRCUS_DOGS.append(SAL_DOG)
CIRCUS_DOGS.append(KIP_DOG)
CIRCUS_DOGS.append(FR_DOG)

print()
print(SAL_DOG.__str__())
print(KIP_DOG.__str__())
print(FR_DOG.__str__())
print()
