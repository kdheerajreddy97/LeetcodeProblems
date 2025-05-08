class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def helper(i, j , pivot):

            if pivot == len(word):
                return True

            if i < 0 or i > m-1 or j < 0 or j > n-1 or board[i][j] != word[pivot]:
                return False
            
            board[i][j] = '#'

            for dir in directions:
                r = i + dir[0]
                c = j + dir[1]
                if helper(r, c, pivot + 1):
                    return True
            board[i][j] = word[pivot]


        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True

        return False
