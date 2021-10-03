from ..gameModel import GameModel
from ..appLib.messageFormatters import (
    msgPlayAgainError, msgPlayAgainAsk, msgPlayHistory
)

async def askPlayAgain(cls: GameModel) -> str:
    """
    return a str 'leave' if user want to leave else 'replay'
    """
    return await validPlayAgain(cls, input(msgPlayAgainAsk()))

async def validPlayAgain(cls: GameModel, action: str) -> str:
    action = action.replace(' ', '').lower()
    if action == 'leave':
        print(msgPlayHistory(cls.win_record))
        return action

    if action != 'play':
        return await validPlayAgain(cls, input(msgPlayAgainError(action)))
    
    return 'replay'
    