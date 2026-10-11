class Solution:
    def reverseBits(self, n: int) -> int:
        # print(bin(n<<1))
        
        binary = " "
        for i in range(32):
            if n &(1<<i):
                binary += "1"
            else:
                binary += '0'
        print(binary)
        res = 0 
        for i, bit in enumerate(binary[::-1]):
            if bit =="1":
                res = res | (1<<i)
        return res