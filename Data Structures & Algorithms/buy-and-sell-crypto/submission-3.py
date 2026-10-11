class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_p = float("inf")
        profit = 0

        for price in prices:
            min_p = min(min_p,price)
            cur_profit = price -min_p
            if profit < cur_profit :
                profit = cur_profit
        return profit