import json

BASE_DIR = r'tic_tac_toe_game3/src/asset/'

settings = json.load(open(BASE_DIR + r'setting_constants.json'))
level_constants = json.load(open(BASE_DIR + r'level_constants.json'))
message = json.load(open(BASE_DIR + r'message.json'))