class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i:i[0])

        res = []
        for x in intervals:

            if not res or  x[0] > res[-1][1]  :
                res.append(x)
            else:
                #overalpping condition
                #merging last list of res
                res[-1][1] = max(res[-1][1],x[1])
        return res