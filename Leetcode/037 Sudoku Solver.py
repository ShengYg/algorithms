class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for row in xrange(len(board)):
            board[row] = list(board[row])
        self.solve(board)
        for row in xrange(len(board)):
            board[row] = "".join(board[row])
        return
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in list('123456789'):
                        if self.is_valid(c, i, j, board):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
                    
    def is_valid(self, c, i, j, board):
        for row in range(9):
            if board[row][j] == c:
                return False
         
        for col in range(9):
            if board[i][col] == c:
                return False
                
        for row in range((i / 3) * 3, (i / 3) * 3 + 3):
            for col in range((j / 3) * 3, (j / 3) * 3 + 3):
                if board[row][col] == c:
                    return False
        return True

#method 2 232ms
class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.row = [[1] * 10 for i in range(9)]
        self.col = [[1] * 10 for j in range(9)]
        self.box = [[[1] * 10 for j in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                v = int(board[i][j])
                self.row[i][v] = self.col[j][v] = self.box[i/3][j/3][v] = 0
        self.BT(0, 0)

    def BT(self, i, j):
        if i == 9:
            return True
        if self.board[i][j] != '.':
            return self.BT(*((i, j+1) if j < 8 else (i+1, 0)))

        for v in range(1, 10):
            if self.row[i][v] and self.col[j][v] and self.box[i/3][j/3][v]:
                self.board[i][j] = str(v)
                self.row[i][v] = self.col[j][v] = self.box[i/3][j/3][v] = 0
                if self.BT(*((i, j+1) if j < 8 else (i+1, 0))): return True
                self.row[i][v] = self.col[j][v] = self.box[i/3][j/3][v] = 1
        self.board[i][j] = '.'
        return False
