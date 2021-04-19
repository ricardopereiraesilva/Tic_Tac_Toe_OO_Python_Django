from tic_tac_toe.problem_domain import move

class Strategy():
	def __init__(self):
		super().__init__()
		self.moveOrder=0
		self.strategyWay=0

	def restoreData(self, arg_move_order, arg_strategy_way):
		self.moveOrder=arg_move_order
		self.strategyWay=arg_strategy_way	

	def get_move_order(self):
		return self.moveOrder
	 
	def get_strategy_way(self):
		return self.strategyWay
	 
	def defineMove(self, state):
		pass
	 
	def getMove1(self, state):
		pass
	 
	def getMove2(self, state):
		pass

	def getFirstMove(self):
		return move.Move(1, 1)
	 	  
	def getMoveThatFillsLine(self, state, aSymbol):
		symbolCounter = 0
		emptyLine = 0
		emptyColumn = 0
		myMove = move.Move(0, 0)
		for x in range(3):
			aLine = x+1
			if (state.occupiedPositionsOnTheLine(aLine) == 2):
				symbolCounter = 0
				emptyLine = 0
				emptyColumn = 0
				for y in range(3):
					aColumn = y+1
					if state.emptyPosition(aLine, aColumn):
						emptyLine = aLine
						emptyColumn = aColumn
					else:
						if (state.getValue(aLine, aColumn) == aSymbol):
							symbolCounter=symbolCounter+1
				if symbolCounter==2:
					myMove = move.Move(emptyLine, emptyColumn)
		return myMove
	
	def getMoveThatFillsColumn(self, state, aSymbol):
		symbolCounter = 0
		emptyLine = 0
		emptyColumn = 0
		myMove = move.Move(0, 0)
		for y in range(3):
			aColumn=y+1
			if (state.occupiedPositionsOnTheColumn(aColumn) == 2):
				symbolCounter = 0
				emptyLine = 0
				emptyColumn = 0
				for x in range(3):
					aLine = x+1
					if state.emptyPosition(aLine, aColumn):
						emptyLine = aLine
						emptyColumn = aColumn
					else:
						if (state.getValue(aLine, aColumn) == aSymbol):
							symbolCounter=symbolCounter+1
				if symbolCounter==2:
					myMove = move.Move(emptyLine, emptyColumn)
		return myMove

	def getMoveThatFillsMainDiagonal(self, state, aSymbol):
		symbolCounter = 0
		emptyLine = 0
		emptyColumn = 0
		myMove = move.Move(0, 0)
		if state.emptyPosition(1, 1):
			emptyLine = 1
			emptyColumn = 1
		else:
			if (state.getValue(1, 1) == aSymbol):
				symbolCounter+=1
		if state.emptyPosition(2, 2):
			emptyLine = 2
			emptyColumn = 2
		else:
			if (state.getValue(2, 2) == aSymbol):
				symbolCounter+=1
		if state.emptyPosition(3, 3):
			emptyLine = 3
			emptyColumn = 3
		else:
			if (state.getValue(3, 3) == aSymbol):
				symbolCounter=symbolCounter+1
		if symbolCounter==2:
			myMove = move.Move(emptyLine, emptyColumn)
		return myMove

	def getMoveThatFillsSecondaryDiagonal(self, state, aSymbol):
		symbolCounter = 0
		emptyLine = 0
		emptyColumn = 0
		myMove = move.Move(0, 0)
		if state.emptyPosition(3, 1):
			emptyLine = 3
			emptyColumn = 1
		else:
			if (state.getValue(3, 1) == aSymbol):
				symbolCounter+=1
		if state.emptyPosition(2, 2):
			emptyLine = 2
			emptyColumn = 2
		else:
			if (state.getValue(2, 2) == aSymbol):
				symbolCounter+=1
		if state.emptyPosition(1, 3):
			emptyLine = 1
			emptyColumn = 3
		else:
			if (state.getValue(1, 3) == aSymbol):
				symbolCounter=symbolCounter+1
		if symbolCounter==2:
			myMove = move.Move(emptyLine, emptyColumn)
		return myMove
	
	
	def getMoveToWin(self, state):
		myMove = None
		firstMove = self.getFirstMove()
		mySymbol = state.getValue((firstMove.getLine()), (firstMove.getColumn()))
		# LINES
		myMove = self.getMoveThatFillsLine(state, mySymbol)
		if (myMove.getLine() != 0):
			return myMove
		# COLUMNS
		myMove = self.getMoveThatFillsColumn(state, mySymbol)
		if (myMove.getLine() != 0):
			return myMove		
		# MAIN DIAGONAL
		myMove = self.getMoveThatFillsMainDiagonal(state, mySymbol)
		if (myMove.getLine() != 0):
			return myMove		
		# SECONDARY DIAGONAL
		myMove = self.getMoveThatFillsSecondaryDiagonal(state, mySymbol)	
		return myMove
	 
	def getMoveThatAvoidsDefeat(self, state):
		myMove = None
		otherSymbol = 1
		firstMove = self.getFirstMove()
		mySymbol = state.getValue((firstMove.getLine()), (firstMove.getColumn()))
		if mySymbol == 1:
			otherSymbol = 2
		# LINES
		myMove = self.getMoveThatFillsLine(state, otherSymbol)
		if (myMove.getLine() != 0):
			return myMove
		# COLUMNS
		myMove = self.getMoveThatFillsColumn(state, otherSymbol)
		if (myMove.getLine() != 0):
			return myMove
		# MAIN DIAGONAL
		myMove = self.getMoveThatFillsMainDiagonal(state, otherSymbol)
		if (myMove.getLine() != 0):
			return myMove
		# SECONDARY DIAGONAL
		myMove = self.getMoveThatFillsSecondaryDiagonal(state, otherSymbol)
		return myMove
	 
	def getAnyPossibleMove(self, state):
		myMove = None
		for x in range(3):
			aLine=x+1
			for y in range(3):
				aColumn=y+1
				if state.emptyPosition(aLine, aColumn):
					
					myMove = move.Move(aLine, aColumn)
					return myMove
		return myMove
	 
	def getBasicMove(self, state):
		self.moveOrder+=1
		myMove = self.getMoveToWin(state)
		if (myMove.getLine() == 0):
			myMove = self.getMoveThatAvoidsDefeat(state)
			if (myMove.getLine() == 0):
				myMove = self.getAnyPossibleMove(state)
		return myMove

	def move3(self, state):
		return self.getBasicMove(state)

