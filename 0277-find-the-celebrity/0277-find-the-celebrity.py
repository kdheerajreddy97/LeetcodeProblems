# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
# Approach1: using indegree and outdegree array
# Time: O(n2); Space: O(n)
# class Solution:
#     def findCelebrity(self, n: int) -> int:
#         indegree = [0] * n

#         for i in range(n):
#             for j in range(n):
#                 if i!=j and knows(i,j) == 1:
#                     indegree[j] += 1
#                     indegree[i] -= 1

#         for i in range(len(indegree)):
#             print(i)
#             if indegree[i] == n-1:
#                 return i
#         else:
#             return -1

# Time: O(n); Space: O(n)
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        # Identify the potential celebrity
        for i in range(1,n):
            if knows(candidate, i):
                candidate = i

        # Verify if the candidate meets the criteria
        count = 0
        for i in range(n):
            if i != candidate and knows(candidate,i) or not knows(i,candidate):
                return -1
        return candidate


