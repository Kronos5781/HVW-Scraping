from ..modules.reportfetcher import ReportFetcher
from ..modules.reportdb import ReportDB
from ..modules.reportamplify import ReportAmplify


class AutoReporterBase:

    def __init__(self):

        self._report_db = ReportDB()
        self._report_fetcher = ReportFetcher(self._report_db)
        self._report_amplify = ReportAmplify()
