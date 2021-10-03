from typing import Optional
from ..gameModel import GameModel
from ..appLib.messageFormatters import msgLeave
from .clearContent import *

def endOrContinue(cls: GameModel, action: str) -> Optional[str]:
    """
    handle all situations including:
    - gameover and user want to leave
    - gameover and user want to play again
    - game is still playing but user want to leave
    """
    if action == 'leave':
        return leave(cls)

    return restart(cls)

def leave(cls: GameModel) -> None:
    clearAll(cls)
    print(msgLeave())
    return

def restart(cls: GameModel) -> str:
    clearSettings(cls)
    return 'replay'