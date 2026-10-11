class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if sum(nums) % 2:
            return False

        #recursion
        # def dfs(i, target):
        #     if i >= n:
        #         return target == 0
        #     if target < 0:
        #         return False
        #     return dfs(i+1,target) or dfs(i+1,target-nums[i])
        
        # return dfs(0,sum(nums)//2)
        
        #DP
        memo = [None] * n
        def dfs(i,target):
            if target == 0:
                 return True
            if i >= n or target < 0:
                return False
            
            memo[i] = (dfs(i+1,target) or dfs(i+1,target-nums[i]))
            return memo[i]

        return dfs(0,sum(nums)//2)







        #solvinfg subset
        # res,sol = [],[]
        # n = len(nums)
        # def dfs(i):
        #     if i >= n:
        #         return res.append(sol.copy())
            
        #     dfs(i+1)
        #     sol.append(nums[i])
        #     dfs(i+1)
        #     sol.pop()
        # dfs(0)
        # print(res)
        # return True
