# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists  = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge(list1, list2))
            lists = mergedLists
        return lists[0]
                
          
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode] ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        pi = float('inf')
        
        while list1 or list2:
            value1 = list1.val if list1 else pi
            value2 = list2.val if list2 else pi
            
            if value1 < value2:
                curr.next = ListNode(value1)
                curr = curr.next
                list1 = list1.next if list1 else None
            
            else:
                curr.next = ListNode(value2)
                curr = curr.next
                list2 = list2.next if list2 else None
        return dummy.next
            