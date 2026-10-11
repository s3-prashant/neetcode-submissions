class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = []
        operators = ['+','-','/','*']

        for token in tokens:
            if token not in operators:
                res.append(int(token))
            
            else:
                if token== '+':
                    res.append(res.pop()+res.pop())
                elif token== '-':
                    a,b= res.pop(),res.pop()
                    res.append(b-a)
                elif token== '*':
                    res.append(res.pop()*res.pop())
                else:
                    a,b= res.pop(),res.pop()
                    res.append(int(b/a))
        return res[-1]