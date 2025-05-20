class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = set()
        no_of_islands = 0

        def dfs(r,c):
            directions = [[0,-1],[-1,0],[0,1],[1,0]]
            for dir in directions:
                dr, dc = dir[0], dir[1]
                if 0 <= r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == "1":
                    if (r + dr, c + dc) not in visited:
                        visited.add((r + dr, c + dc))
                        dfs(r + dr, c + dc)
                        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    if grid[i][j] == "1":
                        no_of_islands += 1
                        dfs(i,j)
        
        return no_of_islands 
        
        