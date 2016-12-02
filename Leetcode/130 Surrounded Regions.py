class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        m, n = len(board), len(board[0])
        queue = [ij for k in range(m) for ij in ((k, 0),(k, n-1))]
        queue.extend([ij for k in range(n) for ij in ((0, k),(m-1, k))])
        while queue:
            i, j = queue.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                queue.extend([(i, j-1), (i, j+1), (i-1, j), (i+1, j)])
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
