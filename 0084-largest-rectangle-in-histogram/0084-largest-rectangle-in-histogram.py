# Brute force: Time O(n2); Space: O(1)
# Monotonic Stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        mystack = [-1]
        for i in range(len(heights)):
            while mystack[-1] != -1 and heights[mystack[-1]] >= heights[i]:
                index = mystack.pop()
                height = heights[index]
                width = i - mystack[-1] - 1
                max_area = max(max_area, height * width)
            mystack.append(i)

        while mystack[-1] != -1:
            index = mystack.pop()
            height = heights[index]
            width = len(heights) - mystack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area



        