class Solution:
    def climbStairs(self, n: int) -> int:
        mem =[None]*n

        def dfs(i):
            if i >=n :
                return i ==n
            if mem[i] is not None:
                return mem[i]
            mem[i] =dfs(i+2)+dfs(i+1)
            return mem[i]
        return dfs(0)
        # def stairs(i):
           
        #     if i >=n:
        #         return i==n
        #     return  stairs(i+1)+stairs(i+2)
        # return stairs(0)
       