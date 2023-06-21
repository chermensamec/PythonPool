
from game import Game
from myPlayer import Cooperator, Cheater, Copycat, Grudger, Detective, SmartPlayer

if __name__ == '__main__':
    game = Game(matches=10)
    game.play(Cheater(), Cooperator())
    game.play(Cheater(), Copycat())
    game.play(Cheater(), Grudger())
    game.play(Cheater(), Detective())
    game.play(Cheater(),SmartPlayer())
    game.play(Cooperator(), Copycat())
    game.play(Cooperator(), Grudger())
    game.play(Cooperator(), Detective())
    game.play(Cooperator(), SmartPlayer())
    game.play(Copycat(), Grudger())
    game.play(Copycat(), Detective())
    game.play(Copycat(), SmartPlayer())
    game.play(Grudger(), Detective())
    game.play(Grudger(), SmartPlayer())
    game.play(Detective(), SmartPlayer())
    game.top3()
    