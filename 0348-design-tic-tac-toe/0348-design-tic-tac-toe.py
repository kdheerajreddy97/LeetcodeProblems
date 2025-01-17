class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
    def checkrow(self, row, player):
        for i in range(self.n):
            if self.board[row][i] != player:
                return False
        return True
        
    def checkcolumn(self, col, player):
        for i in range(self.n):
            if self.board[i][col] != player:
                return False
        return True
        
    def diagonal(self, player):
        for i in range(self.n):
            if self.board[i][i] != player:
                return False
        return True
        
    def antidiagonal(self, player):
        for i in range(self.n):
            if self.board[i][self.n-i-1] != player:
                    return False
        return True

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if (self.checkrow(row, player) or self.checkcolumn(col, player) or (row == col and self.diagonal(player)) or (col == self.n - row - 1 and self.antidiagonal(player))):
            return player
        return 0




# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)