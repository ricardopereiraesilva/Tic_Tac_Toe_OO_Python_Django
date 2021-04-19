from tic_tac_toe.problem_domain import position, move, player, strategy, strategy1, strategy2, strategy3
from tic_tac_toe.problem_domain import boardImage, automaticPlayer, humanPlayer, board

class DatabaseMapper:
    def __init__(self, arg_register):
        super().__init__()
        self.register = arg_register
        self.my_board = board.Board()

    def restore_problem_domain(self):
        self.my_board.setStatus(self.register.match_status)
        self.my_board.setPlayerStatus(self.register.enabled_player, 
                                     self.register.strategy, self.register.move_order, 
                                     self.register.strategy_way)
        self.my_board.setPositionOccupant(1, 1, self.register.p11)
        self.my_board.setPositionOccupant(1, 2, self.register.p12)
        self.my_board.setPositionOccupant(1, 3, self.register.p13)
        self.my_board.setPositionOccupant(2, 1, self.register.p21)
        self.my_board.setPositionOccupant(2, 2, self.register.p22)
        self.my_board.setPositionOccupant(2, 3, self.register.p23)
        self.my_board.setPositionOccupant(3, 1, self.register.p31)
        self.my_board.setPositionOccupant(3, 2, self.register.p32)
        self.my_board.setPositionOccupant(3, 3, self.register.p33)

    def update_register(self):
        boardImage = self.my_board.getState()
        enabled_player = self.my_board.getEnabledPlayer()
        self.register.match_status = self.my_board.getStatus()
        if enabled_player != None:
            self.register.enabled_player = enabled_player.getSymbol()
        else:
            self.register.enabled_player = 0
        self.register.strategy = self.my_board.get_player(2).get_strategy_number()
        self.register.move_order = self.my_board.get_player(2).get_move_order()
        self.register.strategy_way = self.my_board.get_player(2).get_strategy_way()
        self.register.p11 = boardImage.getValue(1, 1)
        self.register.p12 = boardImage.getValue(1, 2)
        self.register.p13 = boardImage.getValue(1, 3)
        self.register.p21 = boardImage.getValue(2, 1)
        self.register.p22 = boardImage.getValue(2, 2)
        self.register.p23 = boardImage.getValue(2, 3)
        self.register.p31 = boardImage.getValue(3, 1)
        self.register.p32 = boardImage.getValue(3, 2)
        self.register.p33 = boardImage.getValue(3, 3)

    def get_response_data(self):
        boardImage = self.my_board.getState()
        response_data = {}
        response_data["0"] = boardImage.getMessage(),
        response_data["1"] = boardImage.getMap(),
        return response_data

    def getState(self):
        self.restore_problem_domain()
        response_data = self.get_response_data()
        return response_data

    def click_position(self, arg_line, arg_column):
        self.restore_problem_domain()
        self.my_board.click(arg_line, arg_column)
        self.update_register()
        self.register.save()
        response_data = self.get_response_data()
        return response_data