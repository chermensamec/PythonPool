'''Module wich simulate play with candy'''
from collections import Counter
from myPlayer import Player

class Game:
    '''Class wich simulate play with candy'''
    def __init__(self, matches = 10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: Player, player2: Player) -> None:
        '''Simulate game betwwen two players'''
        player1.clear_history()
        player2.clear_history()
        for _ in range(self.matches):
            coopper1 = player1.cooperate()
            coopper2 = player2.cooperate()
            print(f'round {_}')
            print(f'{player1}: cooperate {coopper1}')
            print(f'{player2}: cooperate {coopper2}')

            if coopper1 and coopper2:
                self.registry[player1.name] += 2
                self.registry[player2.name] += 2
            elif not coopper1 and coopper2:
                self.registry[player1.name] += 3
                self.registry[player2.name] += -1
            elif coopper1 and not coopper2:
                self.registry[player1.name] += -1
                self.registry[player2.name] += 3
            player1.save_history(coopper2)
            player2.save_history(coopper1)
        print('----------------------------------------')
        print(player1.name, self.registry[player1.name])
        print(player2.name, self.registry[player2.name])

    def top3(self):
        '''Get three top player'''
        print(self.registry.most_common(3))
