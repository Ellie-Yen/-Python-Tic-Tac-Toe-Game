from random import randint

def pickChess(user_chess: str):
    """
    pick a chess that is different to user_chess  
    - user_chess: a char represents user's choice
    """
    i = ord(user_chess) + randint(1, 25)
    if i > 122: # ord('z') = 122
        i -= 26
        
    return chr(i)
    