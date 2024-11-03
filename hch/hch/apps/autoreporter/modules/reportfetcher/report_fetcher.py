from .report_fetcher_base import ReportFetcherBase
from ..reportdb import ReportDB


class ReportFetcher(ReportFetcherBase):

    def __init__(self, report_db: ReportDB):
        super().__init__(report_db)

    def fetch_reports(self) -> None:
        pass
