class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        valid = set()
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    if (i, cur) in valid or (cur,j) in valid or (i/3,j/3,cur) in valid:
                        return False
                    valid.add((i, cur))
                    valid.add((cur, j))
                    valid.add((i/3,j/3,cur))
        return True
