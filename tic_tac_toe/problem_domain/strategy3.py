from tic_tac_toe.problem_domain import strategy
from tic_tac_toe.problem_domain import move

class Strategy3(strategy.Strategy):
	def __init__(self):
		super().__init__()

	def get_strategy_number(self):
		return 3
	 
	def getMove1(self, state):
		self.moveOrder+=1
		myMove = move.Move(1, 1)
		return myMove
	 
	def getMove2(self, state):
		if (state.emptyPosition(3, 3)):
			self.strategyWay = 1
			myMove = self.getBasicMove(state)
		else:
			self.strategyWay = 2
			self.moveOrder+=1
			myMove = move.Move(3, 1)
		return myMove

	def defineMove(self, state):
		if self.moveOrder==0:
			myMove = self.getMove1(state)
		else: 
			if self.moveOrder==1:
				myMove = self.getMove2(state)
			else:
				myMove = self.getBasicMove(state)		
		return myMove	