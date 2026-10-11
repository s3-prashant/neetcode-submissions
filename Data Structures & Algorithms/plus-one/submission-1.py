class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # dig = ""
        # for n in digits:
        #     dig += str(n)
        # print(dig)
        # res=[]
        # dig = str(int(dig)+1)
        # # return str(int(dig)+1).split()
        # for i in dig:
        #     res.append(i)
        # return res

        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                
                digits[i] +=1
                return digits
            digits[i] = 0

        return [1]+digits

