from ..gameModel import GameModel
from .userPlay import userPlay
from .computerPlay import computerPlay
from .checkWinner import checkWinnerAndLineUpPos
from .gameover import gameover

async def playInTurn(cls: GameModel) -> str:
    """
    a recursive playing process as following:
    playerA -> playerB -> check winner. 

    return 'leave' if user want to leave
    else a str of gameover result
    """
    msg: str = None
    if cls.is_user_turn:
        msg = await userPlay(cls)
    else:
        msg = await computerPlay(cls)
        
    if msg == 'leave':
        return msg
        
    print(msg) # about ending player's turn

    # check winner
    winner, strike_pos = checkWinnerAndLineUpPos(cls)
    if winner:
        return(gameover(cls, winner, strike_pos))

    # continue next turn
    return await playInTurn(cls)