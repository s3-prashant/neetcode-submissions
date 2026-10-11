class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            res = float("inf")
            for coin in coins:
                diff = amount - coin
                if diff >= 0:
                    res = min(res, 1+dfs(diff))
            dp[amount] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= float("inf") else minCoins