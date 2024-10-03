from typing import List
from pydantic import BaseModel


class Game(BaseModel):
    gID: str
    sGID: str
    gNo: str
    live: bool
    gToken: str
    gAppid: str
    gDate: str
    gWDay: str
    gTime: str
    gGymnasiumID: str
    gGymnasiumNo: str
    gGymnasiumName: str
    gGymnasiumPostal: str
    gGymnasiumTown: str
    gGymnasiumStreet: str
    gHomeTeam: str
    gGuestTeam: str
    gHomeGoals: str
    gGuestGoals: str
    gHomeGoals_1: str
    gGuestGoals_1: str
    gHomePoints: str
    gGuestPoints: str
    gComment: str
    gGroupsortTxt: str
    gReferee: str
    robotextstate: str


class ClassEntry(BaseModel):
    games: List[Game]


class Content(BaseModel):
    classes: List[ClassEntry]


class ResponseModel(BaseModel):
    content: Content
