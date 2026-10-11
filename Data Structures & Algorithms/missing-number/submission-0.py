class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=list()
        for n in range(len(nums)+1):
            if n not in nums:
                l.append(n)
        print(l)
        return l[0]