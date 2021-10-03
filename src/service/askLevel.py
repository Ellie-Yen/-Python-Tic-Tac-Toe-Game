from ..gameModel import GameModel
from ..appLib.constants import level_constants
from ..appLib.messageFormatters import (
    msgLevelError, msgLevelSuccess, msgLevelAsk
)

async def askLevel(cls: GameModel) -> str:
    """
    return a str 'leave' if user want to leave else msg to display
    """
    return await validLevel(cls, input(msgLevelAsk()))

async def validLevel(cls: GameModel, action: str) -> str:
    action = action.replace(' ', '').lower()
    if action == 'leave':
        return action

    cls.level = level_constants.get(action)
    if cls.level == None:
        return await validLevel(cls, input(msgLevelError(action)))
    
    return msgLevelSuccess(action)

