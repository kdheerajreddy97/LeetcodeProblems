# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def check(node, left, right):
            
            if not node: 
                return True
                
            if not (left < node.val and right > node.val):
                return False
            
            return (check(node.left, left, node.val) and 
            check(node.right, node.val, right))
        
        return check(root, float("-inf"), float("inf"))
            
                