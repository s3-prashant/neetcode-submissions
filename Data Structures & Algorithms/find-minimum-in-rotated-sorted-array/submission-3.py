class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0,len(nums)-1
        cur_min= nums[0]
        while l<=r :
            mid = (l+r)//2
            if nums[l] < nums[r]:
                cur_min = min(cur_min,nums[l])
                break
            cur_min = min(cur_min,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid-1

        return cur_min