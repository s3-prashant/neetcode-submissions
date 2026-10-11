# class Solution:
#     def isHappy(self, n: int) -> bool:

#         visit = set()
#         while n not in visit:
#             visit.add(n)
#             n = self.sumOfsquares(n)
#             if n==1:
#                 return True
#             return False

#     def sumOfsquares(self,n):
#             output = 0
#             while n:
#                 digit = n%10
#                 digit = digit**2
#                 output += digit
#                 n = n//10
#             return output
        

#         # res=0
#         # for i in str(n):
#         #     res += int(i)**2
        
#         # if res == 1:
#         #     return True
#         # return False


class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        power = lam = 1
        
        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            fast = self.sumOfSquares(fast)
            lam += 1
        return True if fast == 1 else False
    
    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output