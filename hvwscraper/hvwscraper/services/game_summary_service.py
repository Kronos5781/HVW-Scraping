import requests
from datetime import datetime as dt

from ..models import game_summary as game_summary_models


class GamerSummaryService:

    def __init__(self) -> None:
        pass

    def get_game_summary(self, game_id: int) -> game_summary_models.GameSummary:

        data = requests.get(f"https://spo.handball4all.de/service/robotext/if_robotext.php?cmd=text&game={game_id}")

        return game_summary_models.GameSummary(**data.json())
