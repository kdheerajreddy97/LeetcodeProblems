class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        cols = set()
        # left up
        left_diagonal = set()
        # right up
        right_diagonal = set()

        def isValid(row, col):
            if col in cols:
                return False
            if (row - col) in left_diagonal:
                return False
            if (row + col) in right_diagonal:
                return False
            return True


        # pivot is the row
        def helper(row):
            if row == n:
                temp = []
                # Append the board as a list to the res list
                for rows in board:
                    temp.append("".join(rows))
                res.append(temp)
                return

            for col in range(n):
                if not isValid(row, col):
                    continue

                # Action - place queen
                board[row][col] = "Q"
                cols.add(col)
                left_diagonal.add(row - col)
                right_diagonal.add(row + col)

                # Recurse - fill up the next row
                helper(row + 1)

                # Backtrack
                board[row][col] = "."
                cols.remove(col)
                left_diagonal.remove(row - col)
                right_diagonal.remove(row + col)


        helper(0)
        return res