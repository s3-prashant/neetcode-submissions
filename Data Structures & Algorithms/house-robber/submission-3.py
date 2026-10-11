class Solution:
    def rob(self, nums: List[int]) -> int:
        

        #dp topdown
        memo = [None]*len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] is not None:
                return memo[i]
            memo[i] = max(dfs(i+1),dfs(i+2)+nums[i])
            return memo[i]
        return dfs(0)
        #recursion

        # def dfs(i):
        #     if i>=len(nums) :
        #         return 0
        #     return max(dfs(i+1),dfs(i+2),nums[i])
        # return dfs(0)
        #bruteforce (fail)
        # res=0
        # if len(nums) <=3:
        #     return max(nums)
        # for i in range(0,len(nums),2):
        #     res += nums[i]
        # return res