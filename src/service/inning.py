from typing import Optional
from ..gameModel import GameModel

from .start import start
from .endOrContinue import endOrContinue
from .askLevel import askLevel
from .askChess import askChess
from .askOrder import askOrder
from .playInTurn import playInTurn
from .askPlayAgain import askPlayAgain

async def inning(cls: GameModel) -> Optional[str]:
    """
    return 'restart' as a signal to start next inning or
    None to leave the game
    """
    process = (
        start,
        askLevel, askChess, askOrder,
        playInTurn,
        askPlayAgain
    )
    
    action: Optional[str] = ""
    for section in process:
        action = await section(cls)
        if action == 'leave':
            break

        # action is an optional str, 
        # format it or it might show 'None' on terminal
        print(f'{action}')

    #_ restart or end the game
    #_ if want to leave, this will return None
    #_ else "replay"
    return endOrContinue(cls, action)