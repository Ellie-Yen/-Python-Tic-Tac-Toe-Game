from ..gameModel import GameModel
from ..appLib.messageFormatters import (
    msgOrderError, msgOrderSuccess, msgOrderAsk
)

async def askOrder(cls: GameModel) -> str:
    """
    return a str 'leave' if user want to leave else msg to display
    """
    return await validOrder(cls, input(msgOrderAsk()))

async def validOrder(cls: GameModel, action: str) -> str:
    action = action.replace(' ', '').lower()
    if action == 'leave':
        return action

    if action not in 'y n':
        return await validOrder(cls, input(msgOrderError(action)))

    cls.is_user_turn = action == 'y'
    return msgOrderSuccess(action)