from typing import Tuple
from ..gameModel import GameModel
from ..appLib.messageFormatters import (
    msgGameover
)

def gameover(cls: GameModel, winner: str, strike_pos: Tuple[Tuple[int]]) -> str:
    """
    return a str display the result of current game.
    - winner: str, key of cls.win_record
    - strike_pos: Tuple[Tuple[int]], represents the positions lined up
    """
    cls.win_record[winner] += 1
    cls.gameover = True
    return msgGameover(winner, strike_pos, cls.board)