# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Preorder Traversal
        def helper(node, string):
            if node is None:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = helper(node.left, string)
                string = helper(node.right, string)
            return string

        return helper(root, '')


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def helper(node_list):
            if node_list[0] == 'None':
                node_list.pop(0)
                return None
            
            root = TreeNode(node_list[0])
            node_list.pop(0)
            root.left = helper(node_list)
            root.right = helper(node_list)
            return root


        node_list = data.split(',')
        root = helper(node_list)
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))