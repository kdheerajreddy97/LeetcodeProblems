# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        points = defaultdict(list)
        
        def dfs(left, right, node):
            
            if not node:
                return
            
            dfs(left - 1, right + 1, node.left)
            dfs(left + 1, right + 1, node.right)
            
            points[(left,right)].append(node.val)
            
        
        dfs(0,0,root)
        
        output = []
        prev = float("-inf")
        
        for key, val in sorted(points.items()):
            if key[0] != prev:
                output.append([])
                
            output[-1].extend(sorted(val))
            prev = key[0]
            
        return output
            
            