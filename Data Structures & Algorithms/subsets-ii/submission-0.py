class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol= []

        def dfs(i):
            if i >=len(nums):
                x=sol[:]
                if x not in res:
                    
                    res.append((x))
                return
            
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
            dfs(i+1)
        nums.sort()
        dfs(0)
        return res