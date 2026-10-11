class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.strip()
        # s.lower()
        l,r=0,len(s)-1
        while l < r :
            while l < r and not self.alnum(s[l]):
                l += 1
                # print(l)
            while r > l and not self.alnum(s[r]):
                r -= 1
            # print(s)
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        return True
            
    def alnum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))
        
