class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
     
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i,len(s2)):
                # if j+1 != len(s1):
                #     continue
                substr = s2[i : j+1]
                print(substr)
                if len(substr) == len(s1):
                    substr = sorted(substr)

                    if substr == s1:
                            return True
        return False



        # s2=sorted(s2)
        # for i in range(len(s1)):
        #     if s1[i] != s2[i]:
        #         return False
        # return True

                