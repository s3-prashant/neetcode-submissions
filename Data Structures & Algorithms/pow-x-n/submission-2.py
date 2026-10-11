class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0:
            return 1
        if n == 1:
            return x
        cur = n
        n= abs(n)
        while n:
            res *= x
            n -=1
        return res if cur > 0 else 1/res