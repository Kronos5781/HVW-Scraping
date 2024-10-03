from pydantic import BaseModel
from typing import Optional


class GameSummaryRobotText(BaseModel):
    text: Optional[str]


class GameSummary(BaseModel):
    robotext: GameSummaryRobotText
