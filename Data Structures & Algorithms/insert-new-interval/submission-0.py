class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #newinterval is less than current intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #if newInterval is greater than interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            #if newInterval is overlapping
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),
                                max(newInterval[1],intervals[i][1])]
        #at end if newInterval is not added to res
        res.append(newInterval)
        return res
             