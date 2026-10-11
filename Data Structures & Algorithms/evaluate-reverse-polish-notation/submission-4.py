class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=['+','/','-','*']
        stack=[]
        for c in tokens:
            if c == '+':
                # stack.append(stack[-1]+stack[-2])
                stack.append(stack.pop()+stack.pop())
                print(stack)
            elif c == '-':
                # stack.append(stack[-2]-stack[-1])
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
                print(stack)

            elif c == '*':
                # stack.append(stack[-1]*stack[-2])
                stack.append(stack.pop()*stack.pop())                
                print(stack)

            elif c == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
                # stack.append(int(stack[-2]/stack[-1]))
                print(stack)
            else:
                stack.append(int(c))
        return stack[-1]
        # ans=0
        # for i in tokens:
        #     if i in s and res:
        #         if i == '+':
        #             add += res[-1]+res[-2]
        #             ans= add
        #             print(ans)
        #         elif i == '-':
        #             sub = (res[-1]-res[-2])
        #             ans =sub
        #             print("sub",ans)

        #         elif i == '*':
        #             mul = res[-1]*res[-2]
        #             ans =mul
        #             print(ans)

        #         else:
        #             div= int(res[-2]/res[-1])
        #             print(div)
        #             ans = int(ans/div)
        #     else:
        #         res.append(int(i))
        # return ans