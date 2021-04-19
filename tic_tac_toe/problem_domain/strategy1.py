from tic_tac_toe.problem_domain import strategy
from tic_tac_toe.problem_domain import move

class Strategy1(strategy.Strategy):
	def __init__(self):
		super().__init__()

	def get_strategy_number(self):
		return 1

	def getMove1(self, state):
		self.moveOrder+=1
		myMove = move.Move(1, 1)
		return myMove
	 
	def getMove2(self, state):
		self.moveOrder+=1
		if state.occupiedPosition(2, 2):
			self.strategyWay = 3
			myMove = move.Move(3, 3)
		else:
			if ((state.occupiedPosition(2, 1)) or (state.occupiedPosition(2, 3)) or (state.occupiedPosition(3, 1)) ):
				self.strategyWay = 2
				myMove = move.Move(1, 3)
			else:
				self.strategyWay = 1
				myMove = move.Move(3, 1)
		return myMove

	def getMove3Way1(self, state):
		self.moveOrder+=1
		if state.emptyPosition(2, 1):
			myMove = self.getBasicMove(state)
		else:
			if ((state.emptyPosition(3, 2)) and (state.emptyPosition(3, 3))):
				myMove = move.Move(3, 3)
			else:
				myMove = move.Move(1, 3)
		return myMove
	 
	def getMove3Way2(self, state):
		if state.emptyPosition(1, 2):
			myMove = self.getBasicMove(state)
		else:
			self.moveOrder+=1
			if (state.emptyPosition(2, 3)): 
				myMove = move.Move(3, 3)
			else:
				myMove = move.Move(3, 1)
		return myMove
	 
	def getMove3Way3(self, state):
		if state.occupiedPosition(3, 1):
			self.moveOrder+=1
			myMove = move.Move(1, 3)
		else:
			if state.occupiedPosition(1, 3):
				self.moveOrder+=1
				myMove = move.Move(3, 1)
			else:
				myMove = self.getBasicMove(state)
		return myMove
	 
	def getMove3(self, state):
		myMove = None
		if self.strategyWay==1: 
			myMove = self.getMove3Way1(state)
		elif self.strategyWay==2:
			myMove = self.getMove3Way2(state)
		elif self.strategyWay==3:
			myMove = self.getMove3Way3(state)	
		return myMove
	
	def defineMove(self, state):
		if self.moveOrder==0:
			myMove = self.getMove1(state)
		else: 
			if self.moveOrder==1:
				myMove = self.getMove2(state)
			else:
				if self.moveOrder==2:
					myMove = self.getMove3(state)
				else:
					myMove = self.getBasicMove(state)		
		return myMove
	 

 