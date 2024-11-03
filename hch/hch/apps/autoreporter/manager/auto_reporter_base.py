from ..modules.reportfetcher import ReportFetcher
from ..modules.reportdb import ReportDB


class AutoReporterBase:

    def __init__(self):

        self._report_db = ReportDB()
        self._report_fetcher = ReportFetcher(self._report_db)
