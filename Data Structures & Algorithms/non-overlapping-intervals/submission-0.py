class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[0])

        res=[]
        count = 0
        for x in intervals:
            
            if not res or x[0] >= res[-1][1]:
                #non overlapping
                res.append(x)
            else:
                #overalpping
                count+=1
                res[-1][1] = min(res[-1][1],x[1])
            
        return count