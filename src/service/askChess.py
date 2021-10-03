from ..gameModel import GameModel
from ..appLib.pickChess import pickChess
from ..appLib.messageFormatters import (
    msgChessError, msgChessSuccess, msgChessAsk
)

async def askChess(cls: GameModel) -> str:
    """
    return a str 'leave' if user want to leave else msg to display
    """
    return await validChess(cls, input(msgChessAsk()))

async def validChess(cls: GameModel, action: str) -> str:
    action = action.replace(' ', '').lower()
    if action == 'leave':
        return action

    if len(action) != 1 or not action.isalpha():
        return await validChess(cls, input(msgChessError(action)))
    
    cls.chess_map[True] = action
    cls.chess_map[False] = pickChess(action)
    return msgChessSuccess(cls.chess_map[True], cls.chess_map[False])