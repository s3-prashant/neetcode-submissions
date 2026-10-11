class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        check =[]

        if len(nums) == 0:
            return [[]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            #perms = [[3,2],[2,3]]
            for p_list in perms:
                p_list.append(n)
            check.append(perms)
            print(check)
            res.extend(perms)
            nums.append(n)
        return res
        
        
        
        
        # res,sol =[],[]
        # def dfs(i):
        #     if len(sol) == len(nums):
        #         res.append(sol[:])
        #         return
        #     if i >=len(nums):
        #         return
            
        #     # sol.append(nums[i])
        #     for n in nums:
        #         sol.append(n)
            
        #     dfs(i+1)
        #     sol.pop()
        #     dfs(i+1)
        #     print(sol)




        # dfs(0)
        # return(res)