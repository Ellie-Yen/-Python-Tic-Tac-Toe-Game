from typing import List, Tuple, Callable, Optional
from ..gameModel import GameModel
from ..appLib.lineCheckers import *
from ..appLib.constants import settings

PLAYER_MAP = settings['PLAYER_MAP']
COMPUTER = settings['COMPUTER']
USER = settings['USER']
DRAW = settings['DRAW']

def checkWinnerAndLineUpPos(cls: GameModel) -> Tuple[Optional[str],  Optional[Tuple[Tuple[int]]]]:
    """
    Use the last position of chess to determine if there's a winner yet.
    return a tuple of (winner, pos).
    if gameover,
    winner is a constant represent winner or draw 
    pos is a tuple of positions that line up
    otherwise (None, None)
    """
    r, c = cls.last_pos

    #_ check row and col
    check_groups: List[Tuple[Callable, Optional[int]]] = [
        (getPosRow, r),
        (getPosCol, c)
    ]
    
    #_ check diagonals
    if r == c:
        check_groups.append((getPosDiagonalLT, None))
    if r + c == 2:
        check_groups.append((getPosDiagonalRT, None))

    for getPositions, i in check_groups:
        positions = getPositions(i)
        point = str(checkLineUp(cls.board_for_calc, positions))
        if point in PLAYER_MAP:
            return (PLAYER_MAP[point], positions)
    
    #_ check empty (pending)
    for i in range(3):
        for j in range(3):
            if not cls.board_for_calc[i][j]:
                return (None, None)
    
    return (DRAW, ())