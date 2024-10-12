# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        
        slow = head
        fast = head
        
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        
        curr = slow
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        
    
        first = head
        second = prev
        while second.next:
            temp = first.next
            first.next = second
            second = second.next
            first.next.next = temp
            first = temp

        
        # def reverse(slow):
        #     while (slow.next != None):
        #         prev = slow
        #         slow = slow.next
        #         slow.next = prev
        #     return slow
            
            
            
            
        
        
        
        