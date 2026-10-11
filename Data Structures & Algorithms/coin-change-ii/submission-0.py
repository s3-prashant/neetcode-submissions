class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}

        def dfs(i,a):
            if amount == a:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            
            if (i,a) in dp:
                return dp[(i,a)]
            
            dp[(i,a)] = dfs(i,a+coins[i])+dfs(i+1,a)
            return dp[(i,a)]
        return dfs(0,0)
        # memo = [0]*amount

        # def dfs(amount):
        #     if  amount == 0:
        #         return 0
            
        #     minn = float("inf")

        #     for coin in coins:
        #         diff = amount-coin
        #         if diff >=0:
        #             minn =min(minn,dfs(diff)+1)
        #     return minn
        # return dfs(amount)



    