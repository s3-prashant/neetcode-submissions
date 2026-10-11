class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur =[]

        def dfs(i,cur,total):
            if i ==len(nums) or total > target:
                return
            if total == target:
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(i,cur,total+nums[i]) 
            #will use only i for repeatation of same number
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,cur,0)
        return res

