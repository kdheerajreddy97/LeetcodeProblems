# Approach 1: Two Pass Time:O(2n)  Space: O(n) (HashMap)
# Approach 2: Single Pass Time:O(n)  Space: O(n) (HashMap)
# Approach 3: Single Pass Time:O(n)  Space: O(1) (No HashMap)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Two Pass
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
#         if not head:
#             return None
#         dict = {}
        
#         curr = head
        
#         while curr:
#             dict[curr] = Node(curr.val)
#             curr = curr.next
            
#         curr = head
        
#         while curr:
#             if curr.next:
#                 dict[curr].next = dict[curr.next]
            
#             if curr.random:
#                 dict[curr].random = dict[curr.random]
            
#             curr = curr.next
        
#         return dict[head]
        
# Single Pass
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        dict = {}
        curr = head
        
        while curr:
            if curr not in dict:
                dict[curr] = Node(curr.val)
            
            if curr.next: 
                if curr.next not in dict:
                    dict[curr.next] = Node(curr.next.val)
                dict[curr].next = dict[curr.next]
                
            if curr.random:
                if curr.random not in dict:
                    dict[curr.random] = Node(curr.random.val)
                dict[curr].random = dict[curr.random]
            
            curr = curr.next
                
        return dict[head]
        