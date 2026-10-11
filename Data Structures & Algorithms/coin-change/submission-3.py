class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        dp = [0]*(amount+1)
        for i in range(1,amount+1):
            minn =float('inf')
            for coin in coins:
                diff =i-coin
                if diff >=0:
                    minn = min(minn,dp[diff]+1)
            dp[i]= minn
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1
        # mem = [0]*amount
        # def dfs(amount):
        #     if amount==0 :
        #         return 0
        #     minn = float('inf')
        #     for coin in coins:
        #         diff = amount-coin
        #         if diff >= 0:
                    
        #             minn = min(minn, 1+dfs(diff))
        #     return minn
                

        # res = dfs(amount)
        # return res if res < float('inf')  else -1

        # def dfs(amount):
        #     if amount ==0:
        #         return 0
        #     res= 1e9
        #     for coin in coins:
        #         if amount-coin>=0:
        #             res = min(res,1+dfs(amount-coin))
        #     return res

        # mincoins =dfs(amount)
        # return -1 if mincoins >=1e9 else mincoins
        
        