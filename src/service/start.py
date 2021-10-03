from ..gameModel import GameModel
from ..appLib.messageFormatters import msgWelcome

async def start(cls: GameModel) -> None:
    return msgWelcome()