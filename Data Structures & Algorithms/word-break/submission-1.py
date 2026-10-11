class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {len(s) : True}
        def dfs(i):
            if i in memo :
                 return memo[i]
            for w in wordDict:
                if (i+len(w)) <= len(s):
                    if s[i:i+len(w)] == w:
                        if dfs(i+len(w)):
                            memo[i] = True
                            return True
            memo[i] = False              
            
            return memo[i]
        return dfs(0)
        #recursive hashset
        # hashset =  set(wordDict)

        # def dfs(i):
        #     if i == len(s):
        #         return True
            
        #     for j in range(i,len(s)):
        #         if s[i:j+1] in hashset:
        #             if dfs(j+1):
        #                 return True
        #     return False

        # return dfs(0)