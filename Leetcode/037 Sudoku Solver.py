class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
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
