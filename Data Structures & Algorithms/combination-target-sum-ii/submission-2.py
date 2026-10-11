class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res,sol =[],[]
        def dfs(i,sol,total):
            if total==target and sol[:] not in res:
                res.append(sol[:])
                return
            if i >=len(candidates) or total > target:
                return
            sol.append(candidates[i])
            dfs(i+1,sol,total+candidates[i])
            sol.pop()
            dfs(i+1,sol,total)
        candidates.sort()
        dfs(0,sol,0)
        return res
            