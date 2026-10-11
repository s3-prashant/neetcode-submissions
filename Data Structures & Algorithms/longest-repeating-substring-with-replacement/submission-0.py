class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        for i in range(len(s)):
            charset = set()
            maxf = 0 
            count = dict()
            for j in range(i,len(s)):
                
                count[s[j]] = 1 + count.get(s[j],0)
                maxf =  max(maxf,count[s[j]])
                if (j-i+1)-maxf <= k:
                    res=max(res,j-i+1)        

        return res








        # char = {}
        # for i in range(len(s)):
        #     if s[i] not in char:
        #         char[s[i]] = 1
        #     char[s[i]] += 1
        # replace_char = ''
        # for key,v in char.items():
        #     if v <= k:
        #         replace_char = char[key]