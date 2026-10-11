class Solution:
    def rob(self, nums: List[int]) -> int:
     
        n = len(nums)
        if n==0: return 0
        if n ==1 : return nums[0]
        rob = [0]*n
        rob[0] = nums[0]
        rob[1] = max(nums[0],nums[1])     
        res=0
        for i in range(2, n):
           
            rob[i]=max(nums[i]+rob[i-2],rob[i-1])
        return rob[n-1]


        #dp topdown
        # memo = [None]*len(nums)

        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if memo[i] is not None:
        #         return memo[i]
        #     memo[i] = max(dfs(i+1),dfs(i+2)+nums[i])
        #     return memo[i]
        # return dfs(0)
        #recursion

        # def dfs(i):
        #     if i>=len(nums) :
        #         return 0
        #     return max(dfs(i+1),dfs(i+2)+nums[i])
        # return dfs(0)
        #bruteforce (fail)
        # res=0
        # if len(nums) <=3:
        #     return max(nums)
        # for i in range(0,len(nums),2):
        #     res += nums[i]
        # return res