from typing import Union, List, Dict, Tuple
from .constants import settings, message

COMPUTER = settings['COMPUTER']
USER = settings['USER']
DRAW = settings['DRAW']

def boardDisplayer(board: List[List[str]]) -> str:
    return '\n'.join([' '.join(board[row]) for row in range(3)])

def strikeBoardDisplayer(board: List[List[str]], strike_pos: Tuple[Tuple[int]]) -> str:
    """
    - strike_pos: tuples contains positions,
    represents a row/ col/ diagonal to strike
    """
    for r, c in strike_pos:
        board[r][c] = "#"
    
    return boardDisplayer(board)

def msgAsk(question_type: str):
    return message[question_type]['question']

def msgSuccess(question_type: str, *display_args):
    """
    - display_args: list of items to show in the reply,
    amount is depended on the reply sentence
    """
    return message[question_type]['reply'].format(*display_args)

def msgInputError(user_input: str, question_type: str):
    """
    - question_type: key in message
    """
    return message['error']['input'].format(
        user_input, 
        message[question_type]['question']
    )

def msgWelcome():
    return message['welcome']

def msgLeave():
    return message['leave']

def msgPlayAgainAsk():
    return msgAsk('ask_play_again')

def msgPlayAgainError(user_input: str):
    return msgInputError(user_input, 'ask_play_again')

def msgLevelAsk():
    return msgAsk('level')

def msgLevelSuccess(level: str):
    return msgSuccess('level', level)

def msgLevelError(user_input: str):
    return msgInputError(user_input, 'level')

def msgChessAsk():
    return msgAsk('chess')

def msgChessSuccess(chess_for_user: str, chess_for_computer: str):
    return msgSuccess('chess', chess_for_user, chess_for_computer)

def msgChessError(user_input: str):
    return msgInputError(user_input, 'chess')

def msgOrderAsk():
    return msgAsk('order')

def msgOrderSuccess(action: str):
    return message['order']['reply'][action]

def msgOrderError(user_input: str):
    return msgInputError(user_input, 'order')

def msgUserTurnBegin(chess: str):
    return msgAsk('user_turn').format(chess)

def msgUserTurnEnd(chess: str, row: int, col: int, board: List[List[str]]):
    return msgSuccess('user_turn', chess, row, col, boardDisplayer(board))

def msgPositionInputError(user_input: str, chess: str):
    return msgInputError(user_input, 'user_turn').format(chess)

def msgPositionOccupiedError(row: int, col: int):
    return message['error']['position'].format(row, col)

def msgComputerTurnBegin(chess: str):
    return msgAsk('computer_turn').format(chess)

def msgComputerTurnEnd(chess: str, row: int, col: int, board: List[List[str]]):
    return msgSuccess('computer_turn', chess, row, col, boardDisplayer(board))

def msgGameover(winner: str, strike_pos: Tuple[Tuple[int]], board: List[List[str]]):
    """
    - strike_pos: tuples contains positions,
    represents a row/ col/ diagonal to strike
    """
    return (
        message["winner"][winner].format(strikeBoardDisplayer(board, strike_pos))
    )

def msgPlayHistory(win_record: Dict[str, int]):
    user_win = win_record[USER]
    comp_win = win_record[COMPUTER]
    draw = win_record[DRAW]
    total = user_win + comp_win + draw
    return message['show_record'].format(
        total,
        user_win, user_win / total,
        comp_win, comp_win / total,
        draw, draw / total
    )







