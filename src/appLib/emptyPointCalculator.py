from typing import List, Set, Tuple

def emptyPointCalculator(board: List[List[int]]) -> List[Set[Tuple[int]]]:
    """
    Used to test if anyone's about to line up in next turn 
    and get the empty positions.

    For each empty grid, calculate the points represent its neighbors
    in row / col (/ diagonal) directions.
    - if a row is [1, 0, 1], the empty grid, 0, has 1 & 1 = 1 point in row.
    - if a row is [0, 2, 1], the empty grid, 0, has 2 & 1 = 0 point in row.
    For each points, list the empty grids that have such neighbors.
    """
    point_made = [set() for _ in range(3)]

    for r in range(3):
        for c in range(3):
            if board[r][c]:
                continue

            #_ check row and col
            row_point = board[r][c - 1] & board[r][c - 2]
            col_point = board[r - 1][c] & board[r - 2][c]
            point_made[row_point].add((r, c))
            point_made[col_point].add((r, c))

            #_ check diagonals
            if r == c:
                diagonal_left_top_point = board[r - 1][c - 1] & board[r - 2][c - 2]
                point_made[diagonal_left_top_point].add((r, c))
            
            if r + c == 2:
                diagonal_right_top_point = board[r - 1][c - 2] & board[r - 2][c - 1]
                point_made[diagonal_right_top_point].add((r, c))
                
    return point_made
