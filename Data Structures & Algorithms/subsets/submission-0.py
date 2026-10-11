class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        sol,res=[],[]
        def dfs(i):
            if i>=len(nums):
                res.append(sol[:])
                return
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
            dfs(i+1)
        dfs(0)
        return res
        # res=[[]]
        # for n in nums:
        #     for subset in res:
        #         res+=[subset+[n]]
        # return res