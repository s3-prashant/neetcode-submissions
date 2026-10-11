class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = {'}':'{',']':'[',')':'('}
        res = []
        for ch  in s:
            if ch in stack:
                if res and res[-1]== stack[ch]:
                    res.pop()
                else:
                    return False
            else:
                res.append(ch)
        return True if not res else False