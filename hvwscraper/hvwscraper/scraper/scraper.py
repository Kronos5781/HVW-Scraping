from typing import List
from datetime import datetime as dt

from .scraper_base import ScraperBase
from ..models import games as games_models


class Scraper(ScraperBase):

    def __init__(self) -> None:
        super().__init__()

    def scrape(self, start: dt, stop: dt) -> None:

        monday_l = self._get_monday_l(start, stop)

        # get games
        games_l: List[games_models.Game] = []
        for i, monday in enumerate(monday_l):
            games_l += self.games_service.get_games(monday)
            print(f"Got games for {monday.strftime('%Y-%m-%d')} ({i+1}/{len(monday_l)})")

        # get reports
        for i, game in enumerate(games_l):
            self._get_and_save_game_report(game, monday)
            print(f"Got report for {game.gHomeTeam} vs {game.gGuestTeam} ({i+1}/{len(games_l)})")
