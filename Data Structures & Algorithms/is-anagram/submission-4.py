class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for ch in range(len(s)):
            s_dict[s[ch]] = s_dict.get(s[ch],0)+1
            t_dict[t[ch]] = t_dict.get(t[ch],0)+1
        
        return s_dict==t_dict