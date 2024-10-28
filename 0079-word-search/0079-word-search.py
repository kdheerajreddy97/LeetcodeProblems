class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        
        
        for i in range(self.m):
            for j in range(self.n):
                if self.helper(i, j, word):
                    return True
        return False
        
        
    def helper(self, i, j, suffix):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        # Base Case
        if len(suffix) == 0:
            return True
            
            #Check bounds
        if i < 0 or i == self.m or j < 0 or j == self.n or self.board[i][j] != suffix[0]:
            return False
            
        self.board[i][j] = "#"
            
            #Recurse
        for x, y in directions:
            if self.helper(i+x, j+y, suffix[1:]):
                return True
                
        self.board[i][j] = suffix[0]
        return False
            
            
                
                
                
                
                
            
            
            
            