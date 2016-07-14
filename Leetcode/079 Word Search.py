class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_word(board, word, i, j, 0):
                    return True
        return False
    
    def exist_word(self, board, word, i, j, idx):
        if idx == len(word):
            return True
        elif i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return False
        elif board[i][j] != word[idx]:
            return False
        board[i][j] = '#'
        exist = self.exist_word(board, word, i, j + 1, idx + 1) or self.exist_word(board, word, i, j - 1, idx + 1) \
        or self.exist_word(board, word, i - 1, j, idx + 1) or self.exist_word(board, word, i + 1, j, idx + 1)
        board[i][j] = word[idx]
        return exist

	#method 2
    def exist_word(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = "#"
            if i > 0 and self.exist_word(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.exist_word(board, word[1:], i+1, j):
                return True
            if j > 0 and self.exist_word(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.exist_word(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0]
            return False
        else:
            return False
