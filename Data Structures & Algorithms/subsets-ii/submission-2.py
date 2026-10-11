class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = set()
        sol = []
        def dfs(i):
            if i >= len(nums):
                
                    res.add(tuple(sol[:]))
                    return
            dfs(i+1)
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
        nums.sort()
        dfs(0)
        return [list(n) for n in res]










        # res = []
        # sol= []

        # def dfs(i):
        #     if i >=len(nums):
        #         x=sol[:]
        #         if sol[:] not in res:
                    
        #             res.append((x))
        #         return
            
        #     sol.append(nums[i])
        #     dfs(i+1)
        #     sol.pop()
        #     dfs(i+1)
        # nums.sort()
        # dfs(0)
        # return res