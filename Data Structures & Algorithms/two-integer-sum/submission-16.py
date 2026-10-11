class Solution:
    def twoSum(self, nums: List[int], target: int):
        # hashmap = {}
        # for i in range(len(nums)):

        #     diff = target - nums[i]
        #     if diff in hashmap:
        #         return [hashmap[diff],i]
        #     if nums[i] not in  hashmap:
        #         hashmap[nums[i]] = i



        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[nums[i]] = i