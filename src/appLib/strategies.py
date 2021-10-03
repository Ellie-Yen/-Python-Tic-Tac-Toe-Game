from typing import Callable, List, Set, Tuple, Dict

# _: empty
# C: computer's chess
# P: user's chess
# O: occupied, might be C or P
# ?: any, occupied or empty
# *: place to put

corner = {(0, 0), (0, 2), (2, 0), (2, 2)}
side = {(0, 1), (1, 0), (2, 1), (1, 2)}

def strategy0(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    _ _ _   * _ *
    _ * _   _ O _
    _ _ _   * _ *
    """
    if len(empty) < 5:
        return set()
    
    occupied_corner = corner - empty
    if occupied_corner:
        return set()
    
    if not board[1][1]:
        return {(1, 1)}
    
    return {(0, 0), (0, 2), (2, 0), (2, 2)}

def strategy1(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    _ _ O   _ ? O
    _ O _   ? * ?
    * _ _   _ ? _
    """
    if len(empty) < 5:
        return set()
    
    occupied_corner = corner - empty
    if len(occupied_corner) != 1:
        return corner if not occupied_corner else set()

    if not board[1][1]:
        return {(1, 1)}
    
    r, c = occupied_corner.pop()
    return {(2 - r, 2 - c)}

def strategy2(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    P * _ 
    * C * 
    _ * P
    """
    if len(empty) < 5 or not board[1][1]:
        return set()
    
    for r in (0, 2):
        if (board[r][0] & board[2 - r][2] and
        not (board[2 - r][0] | board[r][2])):
            return side & empty
    
    return set()

def strategy3(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    fill_a / fill_b
    _ O _   _ C _
    C C P   O P O
    * O _   * P _
    """
    res = set()
    if not board[1][1]:
        return res

    for r, c in corner & empty:
        fill_a = board[1][1] & board[1][c]
        opsite_corners = board[2 - r][c] | board[2 - r][2 - c]
        if fill_a and not opsite_corners:
            res.add((r, c))
        
        fill_b = board[1][1] & board[r][1]
        opsite_corners = board[r][2 - c] | board[2 - r][2 - c]
        if fill_b and not opsite_corners:
            res.add((r, c))
    
    return res

def strategy4(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    fill_a / fill_b
    * C _   * _ P
    _ ? ?   P ? ?
    C ? ?   _ ? ?
    """
    res = set()
    for r, c in corner & empty:
        fill_a = board[2 - r][c] & board[r][1]
        adjs = board[1][c] | board[r][2 - c]
        if fill_a and not adjs:
            res.add((r, c))
        
        fill_b = board[1][c] & board[r][2 - c]
        adjs = board[2 - r][c] | board[r][1]
        if fill_b and not adjs:
            res.add((r, c))
    
    return res
    
def strategy5(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    * C _
    C ? ?
    _ ? ?
    """
    res = set()
    if board[1][1]:
        return res

    for r, c in corner & empty:
        fill = board[r][1] & board[1][c]
        adj_corners = board[r][2 - c] | board[2 - r][c]
        if fill and not adj_corners:
            res.add((r, c))
    
    return res

def strategy6(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    fill_a / fill_b
    ? ? C   P C P
    ? _ P   _ _ ?
    * _ C   * ? ? 
    """
    res = set()
    if board[1][1]:
        return res

    for r, c in corner & empty:
        fill_a = board[r][2 - c] & board[2 - r][2 - c]
        adjs = board[1][1] | board[r][1]
        if fill_a and not adjs:
            res.add((r, c))
        
        fill_b = board[2 - r][c] & board[2 - r][2 - c]
        adjs = board[1][1] | board[1][c]
        if fill_b and not adjs:
            res.add((r, c))
    
    return res

def strategy7(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    fill_a / fill_b
    C P _   C ? _
    _ C ?   ? P C
    * ? P   * _ P
    """
    res = set()
    if not board[1][1]:
        return res

    for r, c in corner & empty:
        fill_a = board[1][1] & board[2 - r][c]
        adjs = board[1][c] | board[2 - r][2 - c]
        if fill_a and not adjs:
            res.add((r, c))
        
        fill_b = board[1][1] & board[r][2 - c]
        adjs = board[r][1] | board[2 - r][2 - c]
        if fill_b and not adjs:
            res.add((r, c))
    
    return res

def strategy8(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    C ? ?
    _ P ?
    * _ C
    """
    res = set()
    if not board[1][1]:
        return res

    for r, c in corner & empty:
        fill =  board[r][2 - c] & board[2 - r][c]
        adj_sides = board[r][1] | board[1][c]
        if fill and not adj_sides:
            res.add((r, c))
    
    return res

def strategy9(board: List[List[int]], empty: Set[Tuple[int]]):
    """
    _ P C
    C _ ?
    * ? ?
    """
    res = set()
    if board[1][1]:
        return res

    for r, c in corner & empty:
        fill =  board[1][c] & board[2 - r][2 - c]
        adj = board[1][1] | board[2 - r][c]
        if fill and not adj:
            res.add((r, c))
    
    return res

strategies: Dict[int, Callable] = {
    0: strategy0,
    1: strategy1,
    2: strategy2,
    3: strategy3,
    4: strategy4,
    5: strategy5,
    6: strategy6,
    7: strategy7,
    8: strategy8,
    9: strategy9
}