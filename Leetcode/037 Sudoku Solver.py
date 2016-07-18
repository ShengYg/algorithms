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

#method 72ms bit operation
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        pos, H, V, G = [], [0]*9, [0]*9, [0]*9 #Empty cells'position,horizontal,vertical,grid
        ctoV = {str(i):1 << (i-1) for i in range(1, 10)} #eg:'4'=>1000
        self.vtoC={1 << (i-1): str(i) for i in range(1, 10)} #eg:100=>'3'
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    v = ctoV[c]
                    H[i], V[j], G[i/3*3+j/3] = H[i]|v, V[j]|v, G[i/3*3+j/3]|v
                else:
                    pos += (i,j),   
        posDict={(i,j):[x, self.countOnes(x)] for i, j in pos \
                    for x in [0x1ff & ~(H[i]|V[j]|G[i/3*3+j/3])]} 
        self.slove(board, posDict)

    def countOnes(self, n):
            count = 0
            while n:
                count, n = count + 1 , n & ~( n& (~n + 1))
            return count
    
    def slove(self, board, posDict):
        if len(posDict) == 0:
            return True
        p = min(posDict.keys(), key= lambda x: posDict[x][1]) #
        candidate=posDict[p][0]
        while candidate:
            v = candidate & (~candidate + 1) #get last '1'
            candidate &= ~v
            tmp = self.updata(board, posDict, p, v) #updata board and posDict
            if self.slove(board, posDict): #slove next position
                return True
            self.recovery(board, posDict, p, v, tmp) #backtrack-->recovery
        return False
    
    def updata(self, board, posDict, p, v):
        i, j = p[0], p[1]
        board[i][j] = self.vtoC[v]
        tmp = [posDict[p]]
        del posDict[p]
        for key in posDict.keys(): 
            if i == key[0] or j == key[1] or (i/3,j/3) == (key[0]/3,key[1]/3): #relevant points
                if posDict[key][0]&v: #need modify
                    posDict[key][0] &= ~v
                    posDict[key][1] -= 1
                    tmp += key,  #Record these points.  
        return tmp
    
    def recovery(self, board, posDict, p, v, tmp):
        board[p[0]][p[1]] = '.'
        posDict[p] = tmp[0]
        for key in tmp[1:]:
            posDict[key][0] |= v 
            posDict[key][1] += 1

#method 4 64ms DFS,dict
class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()
    
    def PossibleVals(self):
        a = "123456789"
        d, val = {}, {}
        for i in xrange(9):
            for j in xrange(9):
                ele = self.board[i][j]
                if ele != ".":
                    d[("r", i)] = d.get(("r", i), []) + [ele]
                    d[("c", j)] = d.get(("c", j), []) + [ele]
                    d[(i//3, j//3)] = d.get((i//3, j//3), []) + [ele]
                else:
                    val[(i,j)] = []
        for (i,j) in val.keys():
            inval = d.get(("r",i),[])+d.get(("c",j),[])+d.get((i/3,j/3),[])
            val[(i,j)] = [n for n in a if n not in inval ]
        return val
    
    def Solver(self):
        if len(self.val)==0:
            return True
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[kee]
        for n in nums:
            update = {kee:self.val[kee]}
            if self.ValidOne(n, kee, update): # valid choice
                if self.Solver(): # keep solving
                    return True
            self.undo(kee, update) # invalid choice or didn't solve it => undo
        return False
        
    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        for ind in self.val.keys():
            if n in self.val[ind]:
                if ind[0]==i or ind[1]==j or (ind[0]/3,ind[1]/3)==(i/3,j/3):
                    update[ind] = n
                    self.val[ind].remove(n)
                    if len(self.val[ind])==0:
                        return False
        return True
    
    def undo(self, kee, update):
        self.board[kee[0]][kee[1]]="."
        for k in update:            
            if k not in self.val:
                self.val[k]= update[k]
            else:
                self.val[k].append(update[k])
        return None
