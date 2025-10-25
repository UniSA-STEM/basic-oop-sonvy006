"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset("CryptoToken", "Used to repair or buy rigs")]
        self.__rig = None
        self.__trace = 0

    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace(self):
        return self.__trace

    def decrypt_asset(self):
        if len(self.__inventory) > 0:
            self.__inventory[0].decrypt()
        else:
            print(f"No Assets for {self.__name} to decrypt.")

    def encrypt_asset(self):
        if len(self.__inventory) > 0:
            self.__inventory[0].encrypt()
        else:
            print(f"No Assets for {self.__name} to encrypt.")

    def acquire_rig(self):
        token = None
        for item in self.__inventory:
            if item.get_name() == "CryptoToken":
                token = item

        if token:
            self.__inventory.remove(token)
            self.__rig = Rig(f"{self.__name}'s Rig")
            print(f"Rig has been acquired by:{self.__name}.")
        else:
            print(f"No Rig has been acquired by:{self.__name} due to lack of CryptoTokens.")

    def upgrade_rig(self):
        if self.__rig:
            self.__rig.upgrade()
        else:
            print(f"No Rig has been upgraded by:{self.__name}.")

    def attack(self, target_hacker):
        if self.__rig and target_hacker.get_rig():
            print(f"Attack has been launched by:{self.__name} on {target_hacker.get_name()}!")
            self.__trace += 1
            target_hacker.get_rig().get_hit()
        else:
            print(f"No Attack has been launched by: One of the hackers has no rig!")

    def __str__(self):
        rig_name = self.__rig.get_name() if self.__rig else "No Rig"
        inventory_items = ', '.join([a.get_name() for a in self.__inventory]) or "No Items"
        return(
            f"Hacker: {self.__name}\n"
            f"Rig: {rig_name}\n"
            f"Trace level: {self.__trace}\n"
            f"Inventory: {inventory_items}"
        )