from tic_tac_toe.problem_domain import position
from tic_tac_toe.problem_domain import automaticPlayer
from tic_tac_toe.problem_domain import humanPlayer
from tic_tac_toe.problem_domain import boardImage
from tic_tac_toe.problem_domain import move
import random

#	Board matchStatus
# 1 - game not started (initial message)
# 2 - next player (match in progress)
# 3 - irregular move (match in progress)
# 4 - game with winner
# 5 - game tied

class Board:
	def __init__(self):
		super().__init__()
		self.player1=humanPlayer.HumanPlayer()
		self.player2=automaticPlayer.AutomaticPlayer()
		self.player1.initialize("Você", 1)
		self.player2.initialize("Programa", 2)
		self.matchStatus = 1
		self.positions=[]
		for y in range(3):
			column = []
			for x in range(3):
				column.append(position.Position())
			self.positions.append(column)

	def setPositionOccupant(self, line, column, playerSymbol):
		if playerSymbol==0:
			self.positions[line-1][column-1].setOccupant(None)
		if playerSymbol==1:
			self.positions[line-1][column-1].setOccupant(self.player1)
		if playerSymbol==2:
			self.positions[line-1][column-1].setOccupant(self.player2)

	def setPlayerStatus(self, enabled_player, strategy, move_order, strategy_way):
		if enabled_player==1:
			self.player1.enable(boardImage.BoardImage())
			if self.matchStatus == 4:
				self.player1.setWinner()
		if enabled_player==2:
			self.player2.enable(boardImage.BoardImage())
			if self.matchStatus == 4:
				self.player2.setWinner()
		if strategy!=0:
			self.player2.restore_strategy(strategy, move_order, strategy_way)

	def get_player(self, number):
		if number == 1:
			return self.player1
		else:
			return self.player2

	def getStatus(self):
		return self.matchStatus

	def setStatus(self, value):
		self.matchStatus = value

	def reset(self):
		for x in range(3):
			for y in range(3):
				self.positions[x][y].empty()
		self.player1.reset()
		self.player2.reset()
		self.setStatus(1)

	def evaluateFull(self):
		full = True
		for x in range(3):
			for y in range(3):
				if (not self.positions[x][y].occupied()):
					full = False
		return full
	
	def getWinner(self):
		if (self.player1.getWinner()):
			return self.player1
		else:
			if (self.player2.getWinner()):
				return self.player2
			else:
				return None			
	
	def getPosition(self, aMove):
		x = aMove.getLine() - 1
		y = aMove.getColumn() - 1
		return self.positions[x][y]

	def getEnabledPlayer(self):
		if self.player1.getTurn():
			return self.player1
		else: 
			return self.player2

	def getDisabledPlayer(self):
		if self.player1.getTurn():
			return self.player2
		else: 
			return self.player1

	def evaluateWinner(self, aMove):
		selected = self.getPosition(aMove)	
		p1=None
		p2=None
		#test of the column
		if aMove.getLine()==1:
				p1 = self.positions[1][aMove.getColumn()-1]
				p2 = self.positions[2][aMove.getColumn()-1]		
		elif aMove.getLine()==2:
				p1 = self.positions[0][aMove.getColumn()-1]
				p2 = self.positions[2][aMove.getColumn()-1]
		elif aMove.getLine()==3:
				p1 = self.positions[0][aMove.getColumn()-1]
				p2 = self.positions[1][aMove.getColumn()-1]
		winner = selected.samePlayer(p1, p2)
		if (winner):
			selected.getOccupant().setWinner()
		else:		
			#test of the line
			if aMove.getColumn()==1:
					p1 = self.positions[aMove.getLine()-1][1]
					p2 = self.positions[aMove.getLine()-1][2]
			elif aMove.getColumn()==2:
					p1 = self.positions[aMove.getLine()-1][0]
					p2 = self.positions[aMove.getLine()-1][2]
			elif aMove.getColumn()==3:
					p1 = self.positions[aMove.getLine()-1][0]
					p2 = self.positions[aMove.getLine()-1][1]
			winner = selected.samePlayer(p1, p2)
			if (winner):
				selected.getOccupant().setWinner()
			else:			
				#test of the main diagonal 
				if ((aMove.getLine() == 1) and (aMove.getColumn() == 1)):
					p1 = self.positions[1][1]
					p2 = self.positions[2][2]	
					winner = selected.samePlayer(p1, p2)		
				if ((aMove.getLine() == 2) and (aMove.getColumn() == 2)):
					p1 = self.positions[0][0]
					p2 = self.positions[2][2]
					winner = selected.samePlayer(p1, p2)
				if ((aMove.getLine() == 3) and (aMove.getColumn() == 3)):
					p1 = self.positions[0][0]
					p2 = self.positions[1][1]
					winner = selected.samePlayer(p1, p2)				
				if (winner):
					selected.getOccupant().setWinner()
				else:							
					#test of the secondary diagonal
					if ((aMove.getLine() == 3) and (aMove.getColumn() == 1)):
						p1 = self.positions[1][1]
						p2 = self.positions[0][2]
						winner = selected.samePlayer(p1, p2)
					if ((aMove.getLine() == 2) and (aMove.getColumn() == 2)):
						p1 = self.positions[0][2]
						p2 = self.positions[2][0]
						winner = selected.samePlayer(p1, p2)
					if ((aMove.getLine() == 1) and (aMove.getColumn() == 3)):
						p1 = self.positions[1][1]
						p2 = self.positions[2][0]
						winner = selected.samePlayer(p1, p2)
					if (winner):
						selected.getOccupant().setWinner()

	def getState(self):
		state = boardImage.BoardImage()
		# composing the message
		if (self.getStatus() == 1): 
			state.setMessage("Clique em qualquer posição para iniciar")
		elif (self.getStatus() == 2):
			state.setMessage((self.getEnabledPlayer()).getName() + " deve jogar")	
		elif (self.getStatus() == 3): 
			state.setMessage("jogada irregular - jogue novamente")
		elif (self.getStatus() == 4): 
			state.setMessage((self.getWinner()).getName() + " venceu a partida")
		elif (self.getStatus() == 5): 
			state.setMessage("A partida terminou empatada")
		# obtaining board filling	
		for x in range(3):
			for y in range(3):
				if (self.positions[x][y].occupied()):
					value = (self.positions[x][y].getOccupant()).getSymbol()
					state.setValue((x+1), (y+1), value)			
				else:
					value = 0
					state.setValue((x+1), (y+1), value)
		return state

	def proceedMove(self, aMove):
		selectedPosition = self.getPosition(aMove)
		if selectedPosition.occupied():
			self.setStatus(3)	#	irregular move
		else:
			enabledPlayer = self.getEnabledPlayer()
			disabledPlayer = self.getDisabledPlayer()
			selectedPosition.setOccupant(enabledPlayer)
			self.evaluateWinner(aMove)
			if enabledPlayer.getWinner():	#	winner
				self.setStatus(4)
			else:
				if self.evaluateFull():		#	tied
					self.setStatus(5)
				else:						#	next player
					self.setStatus(2)
					newState = self.getState()
					enabledPlayer.disable()
					newMove = disabledPlayer.enable(newState)
					if (newMove.getLine()!=0):
						self.proceedMove(newMove)

	def startMatch(self):
		self.reset()
		self.setStatus(2)
		initialState = boardImage.BoardImage()
		if random.randint(1,2)==1:
			self.player1.enable(initialState)
		else:
			aMove = self.player2.enable(initialState)
			self.proceedMove(aMove)

	def click(self, line, column):
		if (self.getStatus()==1):
			self.startMatch()
		else:
			if (self.getStatus()==2 or self.getStatus()==3):
				aMove = move.Move(line, column)
				self.proceedMove(aMove)
			else:
				if (self.getStatus()==4 or self.getStatus()==5):
					self.reset()
	