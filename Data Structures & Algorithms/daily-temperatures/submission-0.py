class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        s = []
        count=0
        for i in range(len(t)):
            for j in range(i+1,len(t)):
                if t[j] > t[i]:
                    count = j-i
                    break
            
            s.append(count)
            count=0
        return s
