import time
import random

from typing import List
from datetime import datetime as dt

from .scraper_base import ScraperBase
from ..models import games as games_models
from ..models import scraper_response as scraper_response_models


class Scraper(ScraperBase):

    def __init__(self) -> None:
        super().__init__()

    def scrape(self, start: dt, stop: dt) -> List[scraper_response_models.ScraperResponse]:

        monday_l = self._get_monday_l(start, stop)

        # get games
        games_l: List[games_models.Game] = []
        for i, monday in enumerate(monday_l):
            try:
                games_l += self.games_service.get_games(monday)
                print(f"Got games for {monday.strftime('%Y-%m-%d')} ({i+1}/{len(monday_l)})")
            except Exception as e:
                print(f"Error getting games for {monday.strftime('%Y-%m-%d')}: {e}")

        # get reports
        res_l = []
        for i, game in enumerate(games_l):

            game_summary = self._get_game_report(game)
            if game_summary.robotext.text is None:
                continue

            res = scraper_response_models.ScraperResponse(game=game,
                                                          game_summary=game_summary)
            res_l.append(res)

            print(f"Got report for {game.gHomeTeam} vs {game.gGuestTeam} ({i+1}/{len(games_l)})")

        return res_l
