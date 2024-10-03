import os

from hvwscraper.utils.base_enum import BaseEnum


class Folders(str, BaseEnum):
    DATA = "data"

    @staticmethod
    def create_dirs():
        for folder in Folders:
            os.makedirs(folder, exist_ok=True)


Folders.create_dirs()
