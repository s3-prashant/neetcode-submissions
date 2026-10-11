class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * len(nums)

        # for i in range(1,len(nums)):
        #     res[i] = res[i-1]*nums[i-1]
        # postfix = 1
        # for i in range(len(nums)-1,-1,-1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res

        res=[0]*len(nums)
        prod =1
        zero_count = 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        if zero_count > 1 : return [0] * len(nums)

        for i,num in enumerate(nums):
            if  zero_count:
                if num:
                    res[i] = 0
                    # res.append(0)
                else:
                    res[i] = prod
            else:
                res[i] = prod//num
                # res.append(prod//num)
        return res