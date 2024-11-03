from datetime import datetime as dt
from datetime import timedelta as td

from .report_fetcher_base import ReportFetcherBase
from ..reportdb import ReportDB
from hch.conf import auto_reporter_conf
from hch.utils import Logger


logger = Logger()


class ReportFetcher(ReportFetcherBase):

    def __init__(self, report_db: ReportDB):
        super().__init__(report_db)

    def fetch_reports(self) -> None:

        reports = self._get_reports_from_scraper()

        for report in reports:
            self._report_db.write_report(report)
