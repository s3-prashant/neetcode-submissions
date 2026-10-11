class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  l=[]
        #  for i in nums:
        #     if i in l:
        #         return True
        #     else:
        #         l.append(i)
        #  return False

        # hash_set = set()
        # for num in nums:
        #     if num in hash_set:
        #         return True
        #     hash_set.add(num)
        # return False

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False