from datetime import datetime as dt
from datetime import timedelta as td
from typing import List

from ..base import BaseModule
from ..reportdb import ReportDB
from hch.apps.autoreporter.models import Report
from hch.conf import auto_reporter_conf
from hch.utils import Logger

from hvwscraper import Scraper, ScraperResponse


logger = Logger()


class ReportFetcherBase(BaseModule):

    def __init__(self, report_db: ReportDB):
        super().__init__()

        self._report_db = report_db

        self._scraper = Scraper()

    def _convert_scraper_reports(self, scraper_reports: List[ScraperResponse]) -> List[Report]:

        reports = []
        for scraper_report in scraper_reports:

            date_string = f"{scraper_report.game.gDate} {scraper_report.game.gTime}"
            report = Report(
                game_id=scraper_report.game.gID,
                game_time=dt.strptime(date_string, "%d.%m.%y %H:%M"),
                home_team=scraper_report.game.gHomeTeam,
                guest_team=scraper_report.game.gGuestTeam,
                goals_guest_team=scraper_report.game.gGuestGoals,
                goals_home_team=scraper_report.game.gHomeGoals,
                report_state=scraper_report.game.robotextstate,
                report=scraper_report.game_summary.robotext.text,
            )

            reports.append(report)

        return reports

    def _get_reports_from_scraper(self) -> List[Report]:

        # get dt range
        start = dt.now() - td(days=auto_reporter_conf.DAYS_INTO_PAST)
        stop = dt.now() + td(days=1)
        logger.info(f"Fetching reports from {start} to {stop}")

        # get reports from scraper and convert
        scraper_reports = self._scraper.scrape(start, stop)
        reports = self._convert_scraper_reports(scraper_reports)

        return reports
