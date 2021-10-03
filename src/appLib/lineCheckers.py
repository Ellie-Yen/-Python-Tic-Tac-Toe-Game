from typing import List, Tuple

def checkLineUp(board: List[List[int]], positions: Tuple[Tuple[int]]) -> int:
    """
    For this row / col / diagonal direction, 
    calculate the points represent the current chess positions,
    to determine if someone has lined up
    - if a row0 is [1, 1, 1], then row0 has 1 & 1 & 1 = 1 point.
    - if a col1 is [1, 0, 2], then row0 has 1 & 0 & 2 = 0 point.
    """
    pos1, pos2, pos3 = positions
    return board[pos1[0]][pos1[1]] & board[pos2[0]][pos2[1]] & board[pos3[0]][pos3[1]]

def getPosRow(r: int) -> Tuple[Tuple[int]]:
    return ((r, 0), (r, 1), (r, 2))

def getPosCol(c: int) -> Tuple[Tuple[int]]:
    return ((0, c), (1, c), (2, c))

# actually diagonal won't need args, 
# but in order to execute with above functions more easily, add a dummy arg
def getPosDiagonalLT(dupmmy_arg = None) -> Tuple[Tuple[int]]:
    """
    left top to right bottom
    """
    return ((0, 0), (1, 1), (2, 2))

def getPosDiagonalRT(dupmmy_arg = None) -> Tuple[Tuple[int]]:
    """
    right top to left bottom
    """
    return ((0, 2), (1, 1), (2, 0))
