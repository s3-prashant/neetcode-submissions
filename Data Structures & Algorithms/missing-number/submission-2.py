class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        res = len(nums)
        for n in range(len(nums)+1):
            if n not in hashset:
                return n
        # for i in range(len(nums)):
        #     res += i - nums[i]
        #     print(res)
        # return res