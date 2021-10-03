from typing import List, Tuple, Set
from .constants import settings, level_constants
from .emptyPointCalculator import emptyPointCalculator
from .strategies import strategies
import random

COMPUTER = settings['COMPUTER']
USER = settings['USER']
POINT_MAP = settings['POINT_MAP']
pc: int = POINT_MAP[COMPUTER]
pu: int = POINT_MAP[USER]

def whereToPut(board: List[List[int]], level: int) -> Tuple[int]:
    """
    board: board_for_calc
    return: a tuple of row and col computer puts
    """
    point_made = emptyPointCalculator(board)

    #_ computer will line up in next turn
    if point_made[pc]:
        return random.choice(list(point_made[pc]))
    
    #_ user will line up in next turn
    if point_made[pu]:
        return random.choice(list(point_made[pu]))
    
    #_ no one is about to line up in next turn
    empty = point_made[0]

    # default value for easy level
    pos: Tuple = random.choice(list(empty))
    
    if level == level_constants['easy']:
        return pos
    
    choices: Set[Tuple[int]] = set()
    if level == level_constants['master']:
        master_sets = [
            [2],
            [3, 4, 5]
        ]
        for strategy_set in master_sets:
            for i in strategy_set:
                choices |= strategies[i](board, empty)
            
            if choices:
                return random.choice(list(choices))

    # for middle and master level
    mid_and_master_sets = [
        [0, 1],
        [6, 7, 8, 9]
    ]
    for strategy_set in mid_and_master_sets:
        for i in strategy_set:
            choices |= strategies[i](board, empty)
            
        if choices:
            return random.choice(list(choices))
    
    return pos
    
    
