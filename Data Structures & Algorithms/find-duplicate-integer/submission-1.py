class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow , fast = 0,0
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

        # hash_set ={}
        # for i in nums:
        #     if i in hash_set:
        #         hash_set[i] +=1
        #     else:
        #         hash_set[i] = 1
        # for k,v in hash_set.items():
        #     if v >1:
        #         return k
