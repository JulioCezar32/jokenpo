from match import Match

class DeclareWinner():


    def __init__(self, winner):
        self._winner = winner

    def __str__(self):
        if self._winner == 'Draw':
            return "There is no Winner, please play again"
        else:
            return "The winner is the player who choosed '{}', congratulations for the victory!".format(self._winner)
