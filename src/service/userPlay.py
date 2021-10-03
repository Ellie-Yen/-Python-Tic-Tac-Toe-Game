from typing import Optional, Tuple, List
from ..gameModel import GameModel
from ..appLib.messageFormatters import (
    msgPositionInputError, msgPositionOccupiedError,
    msgUserTurnEnd, msgUserTurnBegin
)
from .putChess import putChess

async def userPlay(cls: GameModel) -> str:
    """
    return an end message.
    re-implement if action is not valid or action is 'leave'
    """
    return await validAction(cls, input(msgUserTurnBegin(cls.chess_map[cls.is_user_turn])))

async def validAction(cls: GameModel, action: str) -> str:
    action = action.replace(" ", "").lower()
    if action == 'leave':
        return action

    user_chess = cls.chess_map[cls.is_user_turn]
    pos = parsePosition(action)
    if not pos:
        return await validAction(cls, input(msgPositionInputError(action, user_chess)))
        
    is_empty = posIsEmpty(cls.board_for_calc, pos)
    if not is_empty:
        return await validAction(cls, input(msgPositionOccupiedError(*pos)))

    putChess(cls, pos)
    return msgUserTurnEnd(user_chess, *pos, cls.board)

def parsePosition(action: str) -> Optional[Tuple[int]]:
    """
    return a tuple (row, col) represents parsed position
    or None if action is not valid
    """
    pos = action.split(',')
    if not len(pos) == 2 or not set(pos).issubset({'0', '1', '2'}):
        return
    
    return (int(pos[0]), int(pos[1]))

def posIsEmpty(board: List[List[int]] ,pos: Tuple[int]):
    r, c = pos
    return board[r][c] == 0