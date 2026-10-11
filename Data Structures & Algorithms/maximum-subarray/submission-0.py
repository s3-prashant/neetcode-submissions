class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # n, res = len(nums), nums[0]
        # for i in range(n):
        #     cur = 0 
        #     for j in range(i,n):
        #         cur += nums[j]
        #         res = max(res,cur)

        # return res

        maxsub, cursum = nums[0],0
        for num in nums:
            if cursum < 0:
                cursum = 0

            cursum += num
            maxsub = max(maxsub,cursum)
        return maxsub