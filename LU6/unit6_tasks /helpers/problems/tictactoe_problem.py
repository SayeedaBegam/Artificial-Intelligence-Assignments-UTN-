class ticTacBoard:
    def __init__(self, init_board):
        self.board = init_board
        self.player = "x"
        self.opponent = "o"
        self.reward = 10
        self.penalty = -10
        self.winner = ""
        self.state = ""

    def evaluate(self):
        # check for win along a row
        for row in range(3):
            if (
                self.board[row][0] != "_"
                and self.board[row][0] == self.board[row][1]
                and self.board[row][1] == self.board[row][2]
            ):
                if self.board[row][0] == self.player:
                    self.winner = self.player
                elif self.board[row][0] == self.opponent:
                    self.winner = self.opponent
                return "game over"

        # check for win along a column
        for col in range(3):
            if (
                self.board[0][col] != "_"
                and self.board[0][col] == self.board[1][col]
                and self.board[1][col] == self.board[2][col]
            ):
                if self.board[0][col] == self.player:
                    self.winner = self.player
                elif self.board[0][col] == self.opponent:
                    self.winner = self.opponent
                return "game over"

        # check for win on a diagonal
        if (
            self.board[0][0] != "_"
            and self.board[0][0] == self.board[1][1]
            and self.board[1][1] == self.board[2][2]
        ):
            if self.board[0][0] == self.player:
                self.winner = self.player
            elif self.board[0][0] == self.opponent:
                self.winner = self.opponent
            return "game over"

        if (
            self.board[0][2] != "_"
            and self.board[0][2] == self.board[1][1]
            and self.board[1][1] == self.board[2][0]
        ):
            if self.board[0][2] == self.player:
                self.winner = self.player
            elif self.board[0][2] == self.opponent:
                self.winner = self.opponent
            return "game over"

        if not self.are_moves_left():
            self.winner = ""
            return "draw"

        return ""

    def print_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print("\n")

    def are_moves_left(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "_":
                    return True
        return False

    def make_move(self, bestMove, player_mark):
        i, j = bestMove[0], bestMove[1]
        self.board[i][j] = player_mark
        return
