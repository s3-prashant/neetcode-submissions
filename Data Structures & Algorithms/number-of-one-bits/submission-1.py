class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        # for i in range(32):
        #     if (1<<i) & n :
        #         res+=1
        # return res
        while n:
            if n&1:
                res+=1
            n >>=1
        return res