from pydantic import BaseModel

from .game_summary import GameSummary
from . games import Game


class ScraperResponse(BaseModel):
    game: Game
    game_summary: GameSummary
