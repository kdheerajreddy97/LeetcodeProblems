# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        countA = 0
        countB = 0
        
        currA = headA
        currB = headB
        while currA.next:
            currA = currA.next
            countA += 1

        while currB.next:
            currB = currB.next
            countB += 1
        
        

        while countA - countB > 0:
            headA = headA.next
            countA -= 1
        while countB - countA > 0:
            headB = headB.next
            countB -= 1
                
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headB
                