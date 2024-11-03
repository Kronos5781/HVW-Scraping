from .auto_reporter_base import AutoReporterBase
from hch.conf import auto_reporter_conf


class AutoReporter(AutoReporterBase):

    def __init__(self):
        super().__init__()

    def run(self) -> None:

        if not auto_reporter_conf.USE_LOCAL_DATA_ONLY:
            self._report_fetcher.fetch_reports()

        reports = self._report_db.get_all_reports()
        for report in reports:
            self._report_amplify.amplify(report)
