class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        #Kadens algo
        res = nums[0]
        curMin,curMax = 1,1
        for num in nums:
            temp = curMax*num
            curMax = max(num*curMax,num*curMin,num)
            curMin = min((temp,num*curMin,num))
            res = max(curMax,res)
        return res


        #MY SOLUTION DIDNT WORK
        # max_p = 1
        # def dfs(i,prod):
        #     nonlocal max_p
        #     if i>= n:
        #         return 0
        #     if prod > max_p:
        #         max_p = prod
        #     return dfs(i+1,max_p*nums[i])
        # dfs(0,nums[0])
        # return max_p

        # res=nums[0]
        # for i in range(n):
        #     cur=nums[i]
        #     res=max(res,cur)
        #     for j in range(i+1,n):
        #         cur *= nums[j]
        #         res= max(cur,res)
        # return res






        # dp = [0]*(n+1)
        # dp[0] = nums[0]
        # if n==0: return dp[0]
        # dp[1] =nums[1]
        # for i in range(2,n+1):

        #     dp[i]=max(dp[i-1]*nums[i],dp[i-2]*nums[i])
        # return dp[n]
