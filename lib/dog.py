#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    name = "Scoop"
    breed = "Pug"
    def __init__(self, name = "Scoop", breed = "Pug"):
        self.set_name(name)
        self.set_breed(breed)
    def set_name(self, name):
        if type(name) == str and name != '' and len(name) < 26:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    def get_name(self):
        return self._name
    def set_breed(self, breed):
        if(breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    def get_breed(self):
        return self._breed
    name = property(get_name, breed)
    breed = property(get_breed, breed)
