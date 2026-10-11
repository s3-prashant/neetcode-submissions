class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res=[]
        for i in range(len(nums)):
            try :
                if k==len(nums)+1 :
                    break
                res.append(max(nums[i:k]))
                k+=1
            except:
                break
            

        return res