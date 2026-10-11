class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s =""
        res =[]
        for i in digits:
            s += str(i)
        s_int = str(int(s)+1)
        print(s_int)
        # for i in s_int:
        #     res.append(i)
        # return res
        return list(s_int)