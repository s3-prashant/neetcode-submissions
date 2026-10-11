class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)-1
        memo1 = [-1] * n
        memo2 = [-1] * n
        house_1 = nums[1:]
        house_n = nums[:-1]
        def dfs(i,nums,memo):
            if i>=n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dfs(i+1,nums,memo),nums[i]+dfs(i+2,nums,memo))
            return memo[i]
        
        dp_1 = dfs(0,house_1,memo1)
        dp_n = dfs(0,house_n,memo2)
        return max(dp_1,dp_n)