from .auto_reporter_base import AutoReporterBase


class AutoReporter(AutoReporterBase):

    def __init__(self):
        super().__init__()

    def run(self) -> None:

        self._report_fetcher.fetch_reports()
        reoports = self._report_db.get_all_reports()
        print(reoports)
