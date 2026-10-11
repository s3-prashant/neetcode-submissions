class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(',']':'[','}':'{'}
        stack =[]
        if len(s)%2 !=0:
            return False
        for i in s:
            if i not in d:
                stack.append(i)
                continue
            if not stack or stack[-1] != d[i]:
                return False
            stack.pop()
        return not stack

