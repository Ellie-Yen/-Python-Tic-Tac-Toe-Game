from typing import Tuple
from ..gameModel import GameModel

def putChess(cls: GameModel, pos: Tuple[int]):
    """
    make in-place operation for both boards
    and switch player.
    Used in playing and test (pretend user and computer)
    """
    cls.last_pos = pos
    r, c = pos
    cls.board_for_calc[r][c] = cls.point_map[cls.is_user_turn]
    cls.board[r][c] = cls.chess_map[cls.is_user_turn]
    cls.is_user_turn = not cls.is_user_turn
    return