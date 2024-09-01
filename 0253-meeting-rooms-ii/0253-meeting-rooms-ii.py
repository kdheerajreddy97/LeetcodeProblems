class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
            
        start.sort()
        end.sort()
        i = 0
        j = 0
        res = 0
        meetings = 0
        while i < len(intervals):
            if end[j] > start[i]:
                i+=1
                meetings+=1
            else:
                meetings -=1
                j+=1
            res = max(res, meetings)
        return res
            
        
    
                