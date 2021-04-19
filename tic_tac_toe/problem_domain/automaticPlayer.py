from tic_tac_toe.problem_domain import player
from tic_tac_toe.problem_domain import strategy1 
from tic_tac_toe.problem_domain import strategy2
from tic_tac_toe.problem_domain import strategy3

class AutomaticPlayer(player.Player):
	def __init__(self):
		super().__init__()
		self.strategy = None

	def restore_strategy(self, arg_strategy, arg_move_order, arg_strategy_way):
		if arg_strategy==1:
			self.strategy = strategy1.Strategy1()
		if arg_strategy==2:
			self.strategy = strategy2.Strategy2()
		if arg_strategy==3:
			self.strategy = strategy3.Strategy3()
		if arg_strategy!=0:
			self.strategy.restoreData(arg_move_order, arg_strategy_way)

	def get_strategy_number(self):
		if self.strategy == None:
			return 0
		else:
			return self.strategy. get_strategy_number()

	def get_move_order(self):
		if self.strategy == None:
			return 0
		else:
			return self.strategy. get_move_order()
	 
	def get_strategy_way(self):
		if self.strategy == None:
			return 0
		else:
			return self.strategy. get_strategy_way()

	def reset(self):
		self.turn = False		#bool
		self.winner = False		#bool
		self.strategy = None

	def define_strategy(self, aState):
		if aState.getEmpty():
			self.strategy = strategy1.Strategy1()
		else:
			if aState.getEmptyCenter():
				self.strategy = strategy2.Strategy2()
			else:
				self.strategy = strategy3.Strategy3()
	 
	def enable(self, aState):
		self.turn = True
		if self.strategy == None:
			self.define_strategy(aState)
		aMove = self.strategy.defineMove(aState)
		return aMove