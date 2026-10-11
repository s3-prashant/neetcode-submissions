class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        hashmap = {}
        l = 0
        # for ch in s:
        #     hashmap[ch] = 1 + hashmap.get(ch,0)
        print (hashmap)
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            w = r-l+1
             # If the current window is not valid, shrink it from the left
            while w - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
                w = r - l + 1  # Update the window size after shrinking
            
            # Update the result with the maximum window size found
            res = max (res,w)
        return res











        # res = 0
        # for i in range(len(s)):
        #     charset = set()
        #     maxf = 0 
        #     count = dict()
        #     for j in range(i,len(s)):
                
        #         count[s[j]] = 1 + count.get(s[j],0)
        #         maxf =  max(maxf,count[s[j]])
        #         if (j-i+1)-maxf <= k:
        #             res=max(res,j-i+1)        

        # return res








        # char = {}
        # for i in range(len(s)):
        #     if s[i] not in char:
        #         char[s[i]] = 1
        #     char[s[i]] += 1
        # replace_char = ''
        # for key,v in char.items():
        #     if v <= k:
        #         replace_char = char[key]