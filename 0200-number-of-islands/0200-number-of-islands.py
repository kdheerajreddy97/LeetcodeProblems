class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        
        rows = len(grid)
        columns = len(grid[0])
        visit = set(())
        islands = 0
        
        def bfs(r,c):
            q = deque()
            
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                r,c = q.popleft()
                
                directions = [[-1,0], [0,1],[1,0],[0,-1]]
                
                for x,y in directions:
                    if (r+x in range(rows) and c+y in range(columns) and grid[r+x] [c+y] == "1" and (r+x,c+y) not in visit):
                        visit.add((r+x,c+y))
                        q.append((r+x,c+y))
                        
            
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands
                    
                    
        