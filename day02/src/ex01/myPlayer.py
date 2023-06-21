'''Module wich describe players'''
class Player:
    '''Base class for players'''
    name = 'player'

    '''Base class of players'''
    def __init__(self) -> None:
        self.number_of_coins = 1

    def cooperate(self):
        '''Make descion of cooperate'''

    def save_history(self, cooperate):
        '''Save history for make a descion for next turn'''

    def clear_history(self):
        '''Clear history of game bofore'''

    def __str__(self):
        return self.name

class Cheater(Player):
    '''Always cheats'''
    name = 'cheater'

    def cooperate(self):
        return False

class Cooperator(Player):
    '''Always cooperates'''
    name = 'cooperator'

    def cooperate(self):
        return True


class Copycat(Player):
    '''Starts with cooperating, but then just repeats whatever the other guy is doing'''
    name = 'copycat'
    def __init__(self):
        super().__init__()
        self.last_round = True

    def clear_history(self):
        self.last_round = True

    def save_history(self, cooperate):
        self.last_round = cooperate

    def cooperate(self):
        return self.last_round

class Grudger(Player):
    '''Starts by always cooperating, but switches to Cheater forever if another
        guy cheats even once'''
    name = 'grudger'
    def __init__(self) -> None:
        super().__init__()
        self.trust = True

    def clear_history(self):
        self.trust = True

    def cooperate(self):
        if self.trust:
            return True
        return False

    def save_history(self, cooperate):
        if not cooperate:
            self.trust = False


class Detective(Player):
    '''First four times goes with [Cooperate, Cheat, Cooperate, Cooperate], and if
        during these four turns another guy cheats even once - switches into a Copycat.
        Otherwise, switches into Cheater himself'''
    name = 'detective'
    def __init__(self) -> None:
        super().__init__()
        self.round = 0
        self.history = []

    def clear_history(self):
        self.round = 0
        self.history = []

    def save_history(self, cooperate):
        self.history.append(cooperate)

    def cooperate(self):
        res = False
        if self.round in [0,2,3]:
            res = True
        elif self.round == 1:
            res = False
        elif False in self.history[:4]:
            res = self.history[-1]
        self.round += 1
        return res

class SmartPlayer(Player):
    '''My own player'''
    name = 'smartPlayer'
    def __init__(self):
        super().__init__()
        self.history = []

    def clear_history(self):
        self.history = []

    def save_history(self, cooperate):
        return self.history.append(cooperate)

    def cooperate(self):
        if len(self.history) == 0:
            return True
        if self.history[0] == False:
            return False
        elif len(self.history) >= 2 and self.history[1] == False:
            return False
        else:
            return True
