"""
File: Hacker.py
Description: Creating and defining hacker class the shows hacker into the grid.
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

class Hacker:
    """
    created a hacker class that shows a hacker that can
    acquire a rig, stores assets , attacks other hackers.

    """
    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset("CryptoToken", "Used to repair or buy rigs")]
        self.__rig = None #at start, the hacker has no rig
        self.__trace = 0 # trace level increase when risks actions are done

    def get_name(self):
        """
        return the name of the hacker
        """
        return self.__name

    def get_inventory(self):
        """
        return the inventory of the hacker including list of asset in hackers inventory
        """
        return self.__inventory

    def get_rig(self):
        """
        return the rig of the hacker
        :return: rig object or nothing.
        """
        return self.__rig

    def get_trace(self):
        """
        returns current trace level of the hacker
        :return: integer
        """
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
        """
        allows hacker to acquire a rig using crypto token.
        """
        token = None
        for item in self.__inventory:
            if item.get_name() == "CryptoToken":
                token = item # finds the first CryptoToken

        if token:
            self.__inventory.remove(token)
            self.__rig = Rig(f"{self.__name}'s Rig")
            print(f"Rig has been acquired by:{self.__name}.")
        else:
            print(f"No Rig has been acquired by:{self.__name} due to lack of CryptoTokens.")

    def upgrade_rig(self):
        """
        updates the hackers rig by 1 level if it exists.
        """
        if self.__rig:
            self.__rig.upgrade()
        else:
            print(f"No Rig has been upgraded by:{self.__name}.")

    def attack(self, target_hacker):
        """
        launches an attack
        """
        if self.__rig and target_hacker.get_rig():
            print(f"Attack has been launched by:{self.__name} on {target_hacker.get_name()}!")
            self.__trace += 1
            target_hacker.get_rig().get_hit()
        else:
            print(f"No Attack has been launched by: One of the hackers has no rig!")

    def __str__(self):
        """
        provides a summary of the hacker's description.
        :return: string showing name, rig, trave level and inventory.
        """
        rig_name = self.__rig.get_name() if self.__rig else "No Rig"
        inventory_items = ', '.join([a.get_name() for a in self.__inventory]) or "No Items"
        return(
            f"Hacker: {self.__name}\n"
            f"Rig: {rig_name}\n"
            f"Trace level: {self.__trace}\n"
            f"Inventory: {inventory_items}"
        )