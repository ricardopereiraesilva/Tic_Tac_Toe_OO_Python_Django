from tic_tac_toe.problem_domain import player
from tic_tac_toe.problem_domain import move

class HumanPlayer(player.Player):
	def __init__(self):
		super().__init__()

	def enable(self, aState):
		self.turn = True
		return move.Move(0, 0)