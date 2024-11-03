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
