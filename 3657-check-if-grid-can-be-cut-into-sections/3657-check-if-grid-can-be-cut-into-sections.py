class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def checkcuts(rectangles, dim):
            gap_count = 0

            rectangles.sort(key=lambda rect: rect[dim])

            farthest_end = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                rect = rectangles[i]

                if farthest_end <= rect[dim]:
                    gap_count += 1

                farthest_end = max(rect[dim + 2], farthest_end) 

            return gap_count >= 2

        
        if checkcuts(rectangles, 0):
            return True
        elif checkcuts(rectangles, 1):
            return True
        else:
            return False