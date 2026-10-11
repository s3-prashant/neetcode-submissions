class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashset = {}
        for n in nums:
            if n not in hashset:
                hashset[n] = 0
            hashset[n] += 1
        print(hashset)
        for k,v in hashset.items():
            if v == 1:
                return k
        return -1