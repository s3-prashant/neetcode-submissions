class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l =0
        sub = []
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i,len(s2)):
                substr = s2[i :j+1]
                print(substr)
                substr = sorted(substr)

                if substr ==s1:
                        return True
        return False
                