class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res= []
        # nums.sort()
        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i-1]:
        #         continue
        #     l,r = i+1,len(nums)-1
        #     while l < r:
        #         threesum = a+nums[l]+nums[r]
        #         if threesum > 0:
        #             r -= 1
        #         elif threesum < 0 :
        #             l += 1
        #         else:
        #             res.append([a,nums[l],nums[r]])
        #             l += 1
        #             while l < r and nums[l] == nums [l-1]:
        #                 l += 1
        # return res
                
        #BF
        # n = len(nums)
        # res=[]
        # sett=set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if (nums[i]+nums[j]+nums[k]) == 0 and tuple(sorted([nums[i],nums[j],nums[k]])) not in sett:

        #                 res.append([nums[i],nums[j],nums[k]])
        #                 sett.add(tuple([nums[i],nums[j],nums[k]]))
        # return res

        res=[]
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            l=i+1
            r=len(nums)-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l+=1
        return res

