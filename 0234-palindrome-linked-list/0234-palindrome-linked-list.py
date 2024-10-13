# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow
        #odd length case
        prev = None
        while mid != None:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
            
        second = prev
        first = head
        while first != slow:
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return False
                
        return True
            
        
        
            
            
            
        