from typing import List
from hch.apps.autoreporter.models import Report


from .report_db_base import ReportDBBase


class ReportDB(ReportDBBase):

    def __init__(self):
        super().__init__()

    def get_all_reports(self) -> List[Report]:
        return []
