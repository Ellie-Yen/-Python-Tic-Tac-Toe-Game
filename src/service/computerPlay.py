
from ..gameModel import GameModel
from ..appLib.whereToPut import whereToPut
from ..appLib.messageFormatters import msgComputerTurnBegin, msgComputerTurnEnd
from .putChess import putChess
import time

async def computerPlay(cls: GameModel) -> str:
    """
    in place modify, return an end message 
    """
    computer_chess = cls.chess_map[cls.is_user_turn]
    print(msgComputerTurnBegin(computer_chess))
    pos = whereToPut(cls.board_for_calc, cls.level)
    putChess(cls, pos)
    time.sleep(2)
    return msgComputerTurnEnd(computer_chess, *pos, cls.board)