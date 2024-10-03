import requests
from datetime import datetime as dt
from pprint import pprint
from typing import List

from ..models import games as games_models


class GamesService:

    def __init__(self) -> None:
        pass

    def get_games(self, monday: dt) -> List[games_models.Game]:

        date_str = monday.strftime("%Y-%m-%d")
        data = requests.get(
            f"https://spo.handball4all.de/service/if_g_json.php?c=482&cmd=pcu&do={date_str}&og=3")

        if len(data.json()) != 1:
            raise ValueError("Data has more than one entry")

        response_model = games_models.ResponseModel(**data.json()[0])

        games_l = []
        for class_entry in response_model.content.classes:
            for game in class_entry.games:
                games_l.append(game)

        return games_l
