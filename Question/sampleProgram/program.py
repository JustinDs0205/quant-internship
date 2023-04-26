from sample import SimpleGame
from answer import ComplexGame

if __name__ == '__main__':
    game = SimpleGame()
    #game = ComplexGame()
    game.setup()
    game.play(15)
