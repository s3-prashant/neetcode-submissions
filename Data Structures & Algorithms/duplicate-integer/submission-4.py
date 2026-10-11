class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        print(hashmap)
        for k in hashmap:
            if hashmap[k] > 1:
                return True
        return False