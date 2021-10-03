async def play():
    from .game import Game
    game = Game()
    await game.run()

