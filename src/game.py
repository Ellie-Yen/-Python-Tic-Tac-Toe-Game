"""
the run process interacting with player
"""
from typing import Optional
from .gameModel import GameModel
from .service.inning import inning

class Game(GameModel):
    def __repr__(self):
        return '\n'.join(f'{item[0]}: {item[1]}' for item in self.__dict__.items())
        
    async def run(self) -> None:
        game_is_continue: Optional[str] = await inning(self)
        if not game_is_continue:
            return
        
        return await self.run()