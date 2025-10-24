"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__level = 0
        self.__storage = [
            Asset("Data Spike", "Used in battles"),
            Asset("Data Spike", "Used in battles"),
            Asset("Removable Drive", "used to extract assets in battles ")
        ]
    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def  get_storage(self):
        return self.__storage

    def is_broken(self):
        return self.__broken



