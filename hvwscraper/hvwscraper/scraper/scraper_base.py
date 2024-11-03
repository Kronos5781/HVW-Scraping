import os

from datetime import datetime as dt
from datetime import timedelta as td
from typing import List
from bs4 import BeautifulSoup


from ..services.game_summary_service import GamerSummaryService
from ..services.games_service import GamesService
from ..models import games as games_models
from ..utils.weekday_translations import WEEKDAY_TRANSLATIONS
from ..constants.folders import Folders
from ..models import game_summary as game_summary_models


class ScraperBase:

    def __init__(self) -> None:

        self.game_summary_service = GamerSummaryService()
        self.games_service = GamesService()

    def _find_first_monday(self, dt: dt) -> dt:
        while dt.weekday() != 0:
            dt += td(days=1)
        return dt

    def _get_monday_l(self, start: dt, stop: dt) -> List[td]:

        # get first monday
        first_monday = self._find_first_monday(start)

        # get all mondays in timeframe
        curr_date = first_monday
        monday_l = []
        while curr_date < stop:
            monday_l.append(curr_date)
            curr_date = curr_date + td(weeks=1)

        return monday_l

    def _get_game_report(self, game: games_models.Game) -> game_summary_models.GameSummary:

        # get report
        game_summary = self.game_summary_service.get_game_summary(game.gID)
        if game_summary.robotext.text is None:
            return game_summary

        # strip html
        soup = BeautifulSoup(game_summary.robotext.text, 'html.parser')
        game_summary.robotext.text = soup.get_text()

        return game_summary
