class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        # res = [0] * len(t)
        res =[]
        
        for i in range(n):
            count = 0 
            for j in range(i+1,n):
                if t[j] > t[i]:
                    count = j-i
                    break
            res.append(count)
        
        return res

        # s = []
        # count=0
        # for i in range(len(t)):
        #     for j in range(i+1,len(t)):
        #         if t[j] > t[i]:
        #             count = j-i
        #             break
            
        #     s.append(count)
        #     count=0
        # return s
