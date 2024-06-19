class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        
        start.sort()
        end.sort()
        
        s, e = 0, 0
        count, meetings = 0, 0
            
        while s < len(start):

            if start[s] < end[e]:
                s +=1
                count+=1
                meetings = max(meetings, count)
            else:
                e += 1
                count -= 1
        return meetings
        