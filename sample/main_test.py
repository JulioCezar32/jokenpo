from playermove import PlayerMove
from match import Match
from congratulations import DeclareWinner

jogador1 = PlayerMove()
jogador2 = PlayerMove()
jogada1 = jogador1.choose_stone()
jogada2 = jogador2.choose_scissor()
game = Match(jogada1,jogada2)
winner = game.getwinner()
result = DeclareWinner(winner)
print(result)
