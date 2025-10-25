"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
print("---- Welcome to Into the Grid (Proper__str__Version)----\n")

hacker1 = Hacker("Cipher")
hacker2 = Hacker("ErrorDestroyer")

print(hacker1)
print(hacker2)

hacker1.acquire_rig()
hacker2.acquire_rig()

hacker1.upgrade_rig()

hacker1.encrypt_asset()
hacker2.decrypt_asset()

hacker1.attack(hacker2)
hacker1.attack(hacker2)

hacker2.get_rig().repair()

print(hacker1)
print(hacker2)



