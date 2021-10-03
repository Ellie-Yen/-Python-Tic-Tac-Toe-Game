"""
the run process interacting with player
"""
from typing import Optional, Dict, List, Tuple
from .appLib.constants import settings

PLAYER_MAP: Dict[str, str] = settings['PLAYER_MAP']
POINT_MAP: Dict[str, int] = settings['POINT_MAP']
COMPUTER: str = settings['COMPUTER']
USER: str = settings['USER']
DRAW: str = settings['DRAW']
USER_POINT: int = POINT_MAP[USER]
COMPUTER_POINT: int = POINT_MAP[COMPUTER]

class GameModel:
    def __init__(self):
        self.level: Optional[int] = None
        self.is_user_turn: Optional[bool] = None
        self.gameover: bool = False
        self.point_map: Dict[bool, int] = {
            True: USER_POINT,
            False: COMPUTER_POINT
        }
        self.chess_map: Dict[bool, str] = {
            True: "",
            False: ""
        }
        self.win_record: Dict[str, int] = {
            COMPUTER: 0,
            USER: 0,
            DRAW: 0
        }

        self.board: List[List[str]] = [['_'] * 3 for _ in range(3)]
        self.board_for_calc: List[List[int]] = [[0] * 3 for _ in range(3)]
        self.last_pos: Tuple[int] = (0, 0)