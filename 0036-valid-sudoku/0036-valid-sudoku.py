class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == ".":
                    continue
                if (board[row][column] in rows[row] or 
                    board[row][column] in columns[column] or 
                    board[row][column] in squares[(row//3, column//3)]):
                    return False
                
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                squares[(row//3, column//3)].add(board[row][column])
                
        return True