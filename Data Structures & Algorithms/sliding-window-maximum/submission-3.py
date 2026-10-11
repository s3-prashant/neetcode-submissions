class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #my soln
        res=[]
        for i in range(len(nums)):
            try :
                if k==len(nums)+1 : #this is to break when window length equals "k"
                    break
                res.append(max(nums[i:k]))
                k+=1 #increment window size to adjust to i [i:k]
            except:
                break
            

        return res


        #neetcode soln
        # output = []
        # for i in range(len(nums)-k+1): 
        #     #loop until lenght-k and plus + to include last element
        #     max_num = nums[i] #initialze 1st number in index "i"

        #     for j in range(i,i+k):
        #         max_num = max(max_num,nums[j])
        #     output.append(max_num)

        # return output


