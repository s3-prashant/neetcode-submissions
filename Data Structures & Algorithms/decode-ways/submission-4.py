class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0
             
            res = dfs(i+1)
            if i+1 < len(s):
                if (s[i] == "1" or
                  s[i] == "2" and s[i+1] in "0123456"):
                 res += dfs(i+2)
            dp[i] = res
            return dp[i]
        return dfs(0)

        
        # d = {'1' : 'A','2' : 'B' , '12':'L'}
        # res = 0
        # res_str =''
        # if s in d :
        #     res+=1
        # for i in s:
        #     if i in d and str(int(i)+1) in d:
        #         res += 1
        #         res_str += d[i]
        #     # elif s in d :
        #     #     res+= 1
        #     print(res_str)
        # return res