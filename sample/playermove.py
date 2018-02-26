class PlayerMove():


    def choose_stone(self):
        self.move = 'Stone'
        return self.move

    def choose_scissor(self):
        self.move = 'Scissor'
        return self.move

    def choose_paper(self):
        self.move = 'Paper'
        return self.move

    def getmove(self):
        return self.move
