# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Brute Force BFS and sort the array to get the k-th largest
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
#         q = deque()
#         q.append(root)
        
#         res = []
#         res.append(root.val)
        
#         while q:
            
#             for i in range(len(q)):
#                 node = q.popleft() 
#                 if node.left:
#                     res.append(node.left.val)
#                     q.append(node.left)
                
#                 if node.right:
#                     res.append(node.right.val)
#                     q.append(node.right)
                
        
#         res.sort()
#         return res[k-1]
    
# Inorder traversal and find the kth element O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node):
            if node == None:
                return
            
            if node:
                dfs(node.left)
            res.append(node.val)
            if node:
                dfs(node.right)
        
        dfs(root)
        
        return res[k-1]