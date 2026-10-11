class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Dp
        min_p =float("inf")
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            elif prices[i]-min_p > max_profit:
                max_profit = prices[i]-min_p
        return max_profit
        
        
        
        #Bruteforce
        # maxprofit = 0

        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         if prices[j]-prices[i] >maxprofit:
        #             maxprofit = prices[j]-prices[i]
        #             #  maxprofit=max(profit,maxprofit)
        # return maxprofit

