# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res = []
        i = 0
        q = deque()
        
        if root:
            q.append(root)
        
        while q:
            level = []
            
            
            for j in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                level.append(node.val)
            
            if (i % 2 == 1):
                res.append(level[::-1])
            else:
                res.append(level)
            i = i + 1
        
        return res
    