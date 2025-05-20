#Approch: DFS traversal; Time: O(V+E); Space: O(V)+ O(V)+ O(V+E)(visited set + recursive stack space + adj list) = O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Create Dictionary with courses and empty lists(prereq)
        # preMap = {i:[] for i in range(numCourses)}
        preMap = defaultdict(list)
        # for i in range(numCourses):
        #     preMap[i] = []
        
        for course, prereq in prerequisites:
            preMap[course].append(prereq) # This dictionary contains the courses and its prerequisites as Key values pair
            
        # visited set
        visit = set()
        
        #implementing dfs; basically detecting cycle
        def dfs(crs):
            # if in visted then there is cycle as we are visting the same node
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            
            for prereq in preMap[crs]:
                if not dfs(prereq):
                    return False
            # Make it empty; since no cycle
            preMap[crs] = []
            visit.remove(crs)
            return True
        
        # There might individual different graphs; hence we need to run dfs on every node
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                
            
        
        
        