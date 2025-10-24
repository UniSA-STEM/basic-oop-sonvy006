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

    def get_hit(self):
        self.__damage += 1
        print(f"Total Damage taken by {self.__name} is {self.__damage}")
        if self.__damage >= 2 and self.__damage == 0:
            self.__broken = True
            print(f"{self.__name} was broken.")

    def repair(self):
        if self.__broken:
            self.__damage = 0
            self.__broken = False
            print(f"Repaired {self.__name}.")
        else:
            print(f"Repair for {self.__name} is not needed.")

    def add_asset(self, asset):
        self.__storage.append(asset)
        print(f"Asset added to {self.__name}.")

    def upgrade(self):
        self.__level += 1
        print(f"Upgraded {self.__name} to {self.__level}.")

