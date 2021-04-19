from tic_tac_toe.problem_domain import strategy
from tic_tac_toe.problem_domain import move

class Strategy2(strategy.Strategy):
	def __init__(self):
		super().__init__()

	def get_strategy_number(self):
		return 2
	
	def getFirstMove(self):
		return move.Move(2, 2)
	 
	def getMove1(self, state):
		self.moveOrder+=1
		myMove = move.Move(2, 2)
		return myMove
		 
	def getMove2(self, state):
		# strategyWay 1
		if ((state.occupiedPositionsOnTheLine(1)== 2) or (state.occupiedPositionsOnTheLine(3)== 2) 
				or (state.occupiedPositionsOnTheColumn(1) == 2) or (state.occupiedPositionsOnTheColumn(3) == 2) ):
			self.strategyWay = 1
			myMove = self.getBasicMove(state)
		else:
			# strategyWay 2
			if ( ( (state.occupiedPosition(1, 2)) and (state.occupiedPosition(3, 2)) ) 
					or ( (state.occupiedPosition(2, 1)) and (state.occupiedPosition(2, 3)) ) ):
				self.strategyWay = 2
				self.moveOrder+=1
				myMove = move.Move(1, 1)
			else:
				# strategyWay 3
				if ( ( (state.occupiedPosition(1, 1)) and (state.occupiedPosition(3, 3)) ) 
						or ( (state.occupiedPosition(3, 1)) and (state.occupiedPosition(1, 3)) ) ):
					self.strategyWay = 3
					self.moveOrder+=1
					myMove = move.Move(2, 1)
				else:
					# strategyWay 4
					if ( ( (state.occupiedPosition(1, 2)) and (state.occupiedPosition(2, 3)) )
							or ( (state.occupiedPosition(1, 2)) and (state.occupiedPosition(3, 3)) ) 
							or ( (state.occupiedPosition(1, 1)) and (state.occupiedPosition(2, 3)) ) ):
						self.strategyWay = 4
						self.moveOrder+=1
						myMove = move.Move(1, 3)
					else:
						# strategyWay 5
						if ( ( (state.occupiedPosition(1, 2)) and (state.occupiedPosition(2, 1)) )
							or ( (state.occupiedPosition(1, 2)) and (state.occupiedPosition(3, 1)) ) 
							or ( (state.occupiedPosition(1, 3)) and (state.occupiedPosition(2, 1)) ) ):
							self.strategyWay = 5
							self.moveOrder+=1
							myMove = move.Move(1, 1)
						else:
							# strategyWay 6
							if ( ( (state.occupiedPosition(3, 2)) and (state.occupiedPosition(1, 3)) )
								or ( (state.occupiedPosition(3, 2)) and (state.occupiedPosition(2, 3)) ) 
								or ( (state.occupiedPosition(3, 1)) and (state.occupiedPosition(2, 3)) ) ):
								self.strategyWay = 6
								self.moveOrder+=1
								myMove = move.Move(3, 3)
							else:
								# strategyWay 7
								self.strategyWay = 7
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

