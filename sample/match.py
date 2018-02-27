import playermove

class Match():

    def __init__(self, player_1, player_2):
        self._player_1 = player_1
        self._player_2 = player_2

    def getwinner(self):
        self.moves = [self._player_1, self._player_2]

        if ('Paper' in self.moves) and ('Stone' in self.moves):
            self.winner = 'Paper'
        elif ('Scissor' in self.moves) and ('Paper' in self.moves):
            self.winner = 'Scissor'
        elif ('Stone' in self.moves) and ('Scissor' in self.moves):
            self.winner = 'Stone'
        else:
            self.winner = 'Draw'
        return self.winner
