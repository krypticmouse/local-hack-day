import os

class TicTacToe:
    def __init__(self):
        self.board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

        self.player = {
            'O': 0,
            'X': 1
        }

    def print_board(self):
        print(self.board[0][0], '|', self.board[0][1], '|', self.board[0][2])
        print('======')

        print(self.board[1][0], '|', self.board[1][1], '|', self.board[1][2])
        print('======')
        
        print(self.board[2][0], '|', self.board[2][1], '|', self.board[2][2])

    def update_board(self, player, move):
        if self.board[move[0]][move[1]] == '':
            self.board[move[0]][move[1]] = 'O' if player == 1 else 'X'
        
        else:
            raise Exception()

    def is_won(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != '':
            return True
        
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[1][1] != '':
            return True

        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[2][i]) and self.board[i][0] != '':
                return True

            elif (self.board[0][i] == self.board[1][i] == self.board[2][i]) and self.board[0][i] != '':
                return True

        return False

    def is_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    return False
        return True

    def start_game(self):
        curr_player = 1
        total_move = 0

        while True:
            os.system('clear')
            self.print_board()
            print('Player', curr_player, 'choose the position(x y): ', end='')
            
            try:
                move = tuple([int(x) for x in input().split()])
                self.update_board(curr_player,move)

            except:
                continue

            total_move += 1
            if total_move >= 5:
                if self.is_won():
                    os.system('clear')
                    self.print_board()
                    print('Player', curr_player, 'won!')
                    break

                if self.is_draw():
                    print('Game is a Draw!')
                    break

            curr_player = 2 if curr_player == 1 else 1


if __name__ == "__main__":
    TicTacToe().start_game()
