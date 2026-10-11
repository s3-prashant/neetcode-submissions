class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return a+b
        res = 0
        carry = 0
        #this works fine for large numbers in java not suitable fo rpython
        # while b!=0:

        #     temp = (a&b) <<1
        #     a = a^b
        #     b = temp
        # return a

        #for python
        mask = 0xFFFFFFFF
        mask_int = 0x7FFFFFFF

        while b!=0:

            carry = (a&b) <<1
            a = (a^b) &mask
            b = carry &mask
        
        if a<=mask_int:
            return a
        else:
            return ~(a^mask)