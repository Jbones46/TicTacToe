class Gamestate:

    def __init__(self):
        self.player_Xs_turn = True
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.key = [0, 0, 0, 0, 0, 0, 0, 0]
        self.d1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.d2 = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
        self.h1 = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.h2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.h3 = [[0, 0, 1], [0, 0, 1], [0, 0, 1]]
        self.v1 = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        self.v2 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        self.v3 = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
        self.tiny_shark = [self.d1, self.d2, self.h1, self.h2, self.h3, self.v1, self.v2, self.v3]

    def check_win_condition(self, x, y):
        for i in range(7):
            if self.tiny_shark[i][x][y] == 1:
                self.key[i] = self.key[i] + self.board[x][y]
                if self.key[i] > 2:
                    return True

        return False

    # returns true if space is empty; false if space is filled
    def check_and_update_board(self, x, y):
        if self.board[x][y] == 0:
            if self.player_Xs_turn == True:
                self.board[x][y] = 1
            else:
                self.board[x][y] = -1
            return True
        else:
            return False
