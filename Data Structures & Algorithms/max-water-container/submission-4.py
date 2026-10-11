# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         amount=0
#         l,r = 0 , len(heights)-1
#         while l < r:
#             amount = max(amount,min(heights[l],heights[r]) * (r-l))
#             if heights[l] < heights[r] :
#                 l+=1
#             elif heights[l] >= heights [r]:
#                 r -= 1
                
#             # else:
#             #     r-=1
#                 # print(amount)
#         return amount

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1,0,-1):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res