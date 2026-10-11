class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j]-prices[i] >0:
                    profit = prices[j]-prices[i]
                    maxprofit =max(profit,maxprofit)
        return maxprofit