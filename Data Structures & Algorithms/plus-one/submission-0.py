class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig = ""
        for n in digits:
            dig += str(n)
        print(dig)
        res=[]
        dig = str(int(dig)+1)
        # return str(int(dig)+1).split()
        for i in dig:
            res.append(i)
        return res
