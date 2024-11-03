import json

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

    def get_all_reports(self) -> List[Report]:
        return []
