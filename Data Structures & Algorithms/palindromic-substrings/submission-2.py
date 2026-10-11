class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res =0
        substring = []
        # residx,reslen =0,0
        for i in range(len(s)):
            l,r =i,i
            while l >=0 and  r< len(s) and s[l]==s[r]:  
                substring.append([s[l:r+1]]) 
                l-=1
                r+=1
                res+=1

            l,r=i,i+1
            while l >=0 and  r< len(s) and s[l]==s[r]:
                l-=1
                r+=1
                res+=1
                substring.append([s[l:r+1]])

        print(substring)
        return res