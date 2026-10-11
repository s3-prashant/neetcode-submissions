class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # min_cost = 0
        n = len(cost)
        # def dfs(i):
        #     if i >= n:

        #         return 0
        #     return cost[i]+ min(dfs(i+1),dfs(i+2))

        # return min(dfs(1),  dfs(0))

        # memo = [-1]*n

        # def dfs(i):
        #     if i >=n :
        #         return 0
        #     if memo[i]!= -1:
        #         return memo[i]
        #     memo[i] = cost[i] + min(dfs(i+1),dfs(i+2))

        #     return memo[i]
        # return min(dfs(1),  dfs(0))

        cost.append(0)

        for i in  range(len(cost)-3,-1,-1):

            cost[i] += min(cost[i+2],cost[i+1])
        return min(cost[0],cost[1])