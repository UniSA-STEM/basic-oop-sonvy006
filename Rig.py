"""
File: Rig.py
Description: Creating and defining rig class which shows hacker's computer details and system.
Author: Vishesh Soni
ID: 1103871387
Username: sonvy006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Rig:
    """
    The rig class shows the hacker's computer set or hacker's rig that a hacker uses.
    """
    def __init__(self, name):
        """
        Initiator method that creates a new rig object.
        :param name:  name of the rig
        """
        self.__name = name
        self.__damage = 0 #monitors the extent of damage rig has taken
        self.__broken = False #shows whether rig is broken or not
        self.__level = 0 # upgrade level of the rig (starts from 0)
        self.__storage = [
            Asset("Data Spike", "Used in battles"),
            Asset("Data Spike", "Used in battles"),
            Asset("Removable Drive", "used to extract assets in battles ")
        ]
    def get_name(self):
        """
        returns the name of the rig
        :return: string name of the rig
        """
        return self.__name

    def get_level(self):
        """
        returns the level of the rig
        :return: integer
        """
        return self.__level

    def get_storage(self):
        """
        returns a list of assets that is stored in the rig
        :return: list of assets
        """
        return self.__storage

    def is_broken(self):
        """
        determines if the rig is broken or not
        :return: true if the rig is broken, false when not.
        """
        return self.__broken

    def get_hit(self):
        """
        increase the rig by 1 when it is attacked.
        when the damage is at level 0 and 2
        :returns: rig is broken.
        """
        self.__damage += 1
        print(f"Total Damage taken by {self.__name} is {self.__damage}")
        if self.__damage >= 2 and self.__level == 0:
            self.__broken = True
            print(f"{self.__name} was broken.")

    def repair(self):
        """
        repairs the rig so that it has no damage taken.
        reset damage to 0 and sets broken to false.
        """
        if self.__broken:
            self.__damage = 0
            self.__broken = False
            print(f"Repaired {self.__name}.")
        else:
            print(f"Repair for {self.__name} is not needed.")

    def add_asset(self, asset):
        """
        adds an asset to the rig
        :param asset: asset to add to the rig
        """
        self.__storage.append(asset)
        print(f"Asset added to {self.__name}.")

    def upgrade(self):
        """
        upgrades the rig to 1 level to improve it.
        """
        self.__level += 1
        print(f"Upgraded {self.__name} to {self.__level}.")

    def __str__(self):
        """
        returns the string representation of the rig
        :return: string representation of the rig including the state and where asset kept.
        """
        assets= ','.join([a.get_name() for a in self.__storage])
        status = "Broken " if self.__broken else "Working"
        return (
            f"Rig '{self.__name}' is {status}.\n"
            f"Level: {self.__level}.\n"
            f"Damage: {self.__damage}.\n"
            f"Stored Assets: {assets}.\n"
        )
