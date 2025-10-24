"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_name(self):
        return self.__name

    def is_encrypted(self):
        return self.__encrypted

    def decrypt(self):
        if self.__encrypted:
            self.__encrypted = False
            print(f"Decrypted {self.__name}")
        else:
            print(f"{self.__name} was already decrypted.")

    def encrypt(self):
        if not self.__encrypted:
            self.__encrypted = True
            print(f"Encrypted {self.__name}")
        else:
            print(f"{self.__name} was already encrypted.")
