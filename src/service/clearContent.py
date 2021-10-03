from ..gameModel import GameModel

def clearSettings(cls: GameModel):
    """
    in-place modify
    """
    for r in range(3):
        for c in range(3):
            cls.board_for_calc[r][c] = 0
            cls.board[r][c] = '_'
    
    cls.chess_map[True] = cls.chess_map[False] = ""
    cls.gameover = False
    cls.level = None
    cls.is_user_turn = None
    cls.last_pos = (0, 0)

def clearAll(cls: GameModel):
    """
    in-place modify
    """
    clearSettings(cls)
    for winner in cls.win_record:
        cls.win_record[winner] = 0
    
    cls.gamestart = False

