class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        min_cost = 0
        n = len(cost)
        def dfs(i):
            if i >= n:

                return 0
            return cost[i]+ min(dfs(i+1),dfs(i+2))

        return min(dfs(1),  dfs(0))