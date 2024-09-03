class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        out =[]
        out.append(intervals[0])
        for i in range(1,len(intervals)):
            lastEnd = out[-1][1]
            start = intervals[i][0]
            
            if start <= lastEnd:
                out[-1][1] = max(lastEnd, intervals[i][1])
            else:
                out.append(intervals[i])
        return out