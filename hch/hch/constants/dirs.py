import os

from ..utils import BaseEnum


class Dirs(str, BaseEnum):
    DATA = "data"
    REPORT_DB = os.path.join(DATA, "report_db")

    @staticmethod
    def create_dirs() -> None:
        for dir_ in Dirs:
            os.makedirs(dir_, exist_ok=True)


Dirs.create_dirs()
