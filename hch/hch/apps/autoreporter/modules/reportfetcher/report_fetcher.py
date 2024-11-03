from datetime import datetime as dt
from datetime import timedelta as td

from .report_fetcher_base import ReportFetcherBase
from ..reportdb import ReportDB
from hch.utils import Logger
from hch.conf import auto_reporter_conf


logger = Logger()


class ReportFetcher(ReportFetcherBase):

    def __init__(self, report_db: ReportDB):
        super().__init__(report_db)

    def fetch_reports(self) -> None:

        start = dt.now() - td(days=auto_reporter_conf.DAYS_INTO_PAST)
        stop = dt.now() + td(days=1)
        logger.info(f"Fetching reports from {start} to {stop}")

        reports = self._scraper.scrape(start, stop)
        print(reports)
        print(len(reports))
