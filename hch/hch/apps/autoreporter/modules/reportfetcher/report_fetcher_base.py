from ..base import BaseModule
from ..reportdb import ReportDB

from hvwscraper import Scraper


class ReportFetcherBase(BaseModule):

    def __init__(self, report_db: ReportDB):
        super().__init__()

        self._report_db = report_db

        self._scraper = Scraper()
