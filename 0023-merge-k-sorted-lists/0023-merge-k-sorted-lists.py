# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##Priority Queue Approach
#Tends to be simpler to implement and may perform better in practice due to the efficient management of the minimum element with a priority queue
#Time Complexity: O(Nlogk)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]])  -> Optional[ListNode]:
        min_heap = []
        
        if len(lists) == 0:
            return None
        for index, node in enumerate(lists):
            if node:
                # sorting based on node.val, then index
                heappush(min_heap,(node.val, index, node))
        
        dummy = ListNode()
        curr = dummy
        while min_heap:
            val, index, node = heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(min_heap, (node.next.val, index, node.next))
        return dummy.next
            


###Divide and Conquer Approach###
#Requires less additional memory because it does not need a priority queue, just temporary merged lists.
#Time Complexity: O(Nlogk)
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
#         if len(lists) == 0:
#             return None

#         while len(lists) > 1:
#             mergedLists  = []
#             for i in range(0, len(lists), 2):
#                 list1 = lists[i]
#                 list2 = lists[i+1] if i+1 < len(lists) else None
#                 mergedLists.append(self.merge(list1, list2))
#             lists = mergedLists
#         return lists[0]
                
          
# Sorting 2 Lists at a time   
#     def merge(self, list1: Optional[ListNode], list2: Optional[ListNode] ) -> Optional[ListNode]:
#         dummy = ListNode()
#         curr = dummy
#         pi = float('inf')
        
#         while list1 or list2:
#             value1 = list1.val if list1 else pi
#             value2 = list2.val if list2 else pi
            
#             if value1 < value2:
#                 curr.next = ListNode(value1)
#                 curr = curr.next
#                 list1 = list1.next if list1 else None
            
#             else:
#                 curr.next = ListNode(value2)
#                 curr = curr.next
#                 list2 = list2.next if list2 else None
#         return dummy.next





            