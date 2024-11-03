from typing import Optional
import os

from datetime import datetime as dt
from pydantic import BaseModel


class Report(BaseModel):
    game_id: str
    game_time: dt
    home_team: str
    guest_team: str
    goals_home_team: str
    goals_guest_team: str
    report_state: str
    report: str
    amplified_report: Optional[str] = None

    def fp(self, tgt_dir: str) -> str:
        return os.path.join(tgt_dir, f"{self.game_id}.txt")
