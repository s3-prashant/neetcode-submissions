class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        
        for i in range(0, len(s2) - len(s1) + 1):
            if s1_count == Counter(s2[i:i+len(s1)]):
                return True
        
        return False