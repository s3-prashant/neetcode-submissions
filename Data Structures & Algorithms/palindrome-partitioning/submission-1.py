class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol,res=[],[]
      
        def dfs(i):
            if i == len(s) :
                res.append(sol[:])
                return

            for j in range(i,len(s)):
                if  isPalindrome(s,i,j):
                    sol.append(s[i:j+1])
                    dfs(j+1)
                    sol.pop()
        def isPalindrome(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l=l+1
                r=r-1
            return True
        dfs(0)
        return res