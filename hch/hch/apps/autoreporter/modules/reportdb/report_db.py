import os

from typing import List
from hch.apps.autoreporter.models import Report
from hch.constants import Dirs
from hch.utils import Logger, files

from .report_db_base import ReportDBBase


logger = Logger()


class ReportDB(ReportDBBase):

    def __init__(self):
        super().__init__()

    def write_report(self, report: Report) -> None:

        fp = report.fp(Dirs.REPORT_DB)
        files.write_json(fp, report.model_dump())

        logger.debug(f"Report written to {fp}")

    def read_report(self, fp: str) -> Report:

        report_dict = files.read_json(fp)
        return Report(**report_dict)

    def get_all_reports(self) -> List[Report]:

        files = os.listdir(Dirs.REPORT_DB)
        report_l = []
        for file in files:
            abs_path = os.path.join(Dirs.REPORT_DB, file)
            report_l.append(self.read_report(abs_path))

        return report_l
