class Gamestate:


    def __init__(self):
        self.player_Xs_turn = True
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.key = [0, 0, 0, 0, 0, 0, 0, 0]
        self.reset_game = False

        # these are the 8 possible victory configurations
        self.d1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.d2 = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
        self.h1 = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.h2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.h3 = [[0, 0, 1], [0, 0, 1], [0, 0, 1]]
        self.v1 = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        self.v2 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        self.v3 = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
        self.tiny_shark = [self.d1, self.d2, self.h1, self.h2, self.h3, self.v1, self.v2, self.v3]


    def reset(self):
        self.player_Xs_turn = True
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.key = [0, 0, 0, 0, 0, 0, 0, 0]
        self.reset_game = False


    def check_win_condition(self, x, y):
        for i in range(len(self.tiny_shark)):
            if self.tiny_shark[i][x][y] == 1:
                self.key[i] = self.key[i] + self.board[x][y]
                if self.key[i] > 2 or self.key[i] < -2:
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


    def print_game_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[j][i] == 1:
                    print('X', end='')
                elif self.board[j][i] == -1:
                    print('O', end='')
                else:
                    print('-', end='')
            print()
