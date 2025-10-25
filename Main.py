"""
File: main.py
Description: This file runs the simulation
and shows how all classes interact with each other,
Author: Vishesh Soni
ID: 110387138
Username: sonvy006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
print("---- Welcome to Into the Grid (Proper__str__Version)----\n")

"""
Creates two hacker objects
"""
hacker1 = Hacker("Cipher")
hacker2 = Hacker("ErrorDestroyer")

"""
Print their initial states
"""
print(hacker1)
print(hacker2)

"""
Hackers acquire rigs 
"""
hacker1.acquire_rig()
hacker2.acquire_rig()

"""
hacker1 cipher upgrades his rig.
"""
hacker1.upgrade_rig()

"""
hacker1 and hacker2 encrypts decrypts his first inventory item.
"""
hacker1.encrypt_asset()
hacker2.decrypt_asset()

"""
hacker1 attacks hacker2
"""
hacker1.attack(hacker2)
hacker1.attack(hacker2)

"""
Hacker2 repairs rig after damage.
"""
hacker2.get_rig().repair()

"""
prints final hacker information
"""
print(hacker1)
print(hacker2)



