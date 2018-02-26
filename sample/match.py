import playermove

class match():


    self.moves = ['Paper', 'Stone']

    def getwinner(self):

        if ('Paper' in self.moves) && ('Stone' in self.moves):
            self.winner = 'Paper'
        else if ('Scissor' in self.moves) && ('Paper' in self.moves):
            self.winner = 'Scissor'
        else if ('Stone' in self.moves) && ('Scissor' in self.moves):
            self.winner = 'Stone'
        else:
            self.winner = 'Draw'
