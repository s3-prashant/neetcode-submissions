class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # newstr = ''
        # for c in s:
        #     if c.isalnum():
        #         newstr += c.lower()
        # return newstr == newstr[::-1]
        # s = newstr
        l,r = 0, len(s)-1
        while l < r:
            print(s[l],s[r])
            if not s[l].isalnum() :
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            # else:
            #     return False
        return True
        