"""
File: Asset.py
Description: Creating and defining class asset that shows digital assets used by hackers and rigs.>
Author: Vishesh Soni
ID: 1103871387
Username: sonvy006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    """
    The asset class represent items in within the simulation
    The actions by hackers or rigs can be encrypting or decrypting of assets.
    """
    def __init__(self, name, description):
        """
        Initiator method that creates a new asset object
        :param name: Asset Name (eg: CryptoToken or Data Spike)
        :param description: A brief text of the use of the asset.
        """
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_name(self):
        """
        returns the name of the asset.
        :return: string name of the asset.
        """
        return self.__name

    def is_encrypted(self):
        """
        checks if the asset is encrypted.
        :return: whether the asset is encrypted or not.
        """
        return self.__encrypted

    def decrypt(self):
        """
        Decrypts the asset
        :return: obtains the encrypted asset and decrypts it.
        """
        if self.__encrypted:
            self.__encrypted = False
            print(f"Decrypted {self.__name}")
        else:
            print(f"{self.__name} was already decrypted.")

    def encrypt(self):
        """
        Encrypts the asset.
        :return: true if encrypted else false.
        """
        if not self.__encrypted:
            self.__encrypted = True
            print(f"Encrypted {self.__name}")
        else:
            print(f"{self.__name} was already encrypted.")

    def __str__(self):
        """
        String representation of the asset.
        breaks down the readable summary of the asset
        including its name and description.
        :return:
        """
        if self.__encrypted:
            return f"{self.__name} was described as '{self.__description}' and is encrypted."
        else:
            return f"{self.__name} was described as '{self.__description}' and is not encrypted."