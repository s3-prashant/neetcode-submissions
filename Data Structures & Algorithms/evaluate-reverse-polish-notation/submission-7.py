class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            stack = []

            for token in tokens:

                if token == "+":
                    print(stack)
                    stack.append(stack.pop()+stack.pop())
                elif token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                elif token == "*":
                    stack.append(stack.pop()*stack.pop())
                elif token == "/":
                    a = stack.pop()
                    b = stack.pop()
                  
                    stack.append(int(float(b)/a))
                else:
                    stack.append(int(token))

            return stack.pop()

        # class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         s=['+','/','-','*']
#         stack=[]
#         for c in tokens:
#             if c == '+':
#                 # stack.append(stack.pop()+stack.pop())
#                 stack.append(stack.pop()+stack.pop())
#                 print(stack)
#             elif c == '-':
#                 # stack.append(stack.pop()-stack.pop())
#                 a,b = stack.pop(),stack.pop()
#                 stack.append(b-a)
#                 print(stack)

#             elif c == '*':
#                 # stack.append(stack.pop()*stack.pop())
#                 stack.append(stack.pop()*stack.pop())                
#                 print(stack)

#             elif c == '/':
#                 a,b = stack.pop(),stack.pop()
#                 stack.append(int(b/a))
#                 # stack.append(int(stack.pop()/stack.pop()))
#                 print(stack)
#             else:
#                 stack.append(int(c))
#         return stack.pop()
#         # ans=0
#         # for i in tokens:
#         #     if i in s and res:
#         #         if i == '+':
#         #             add += res.pop()+res.pop()
#         #             ans= add
#         #             print(ans)
#         #         elif i == '-':
#         #             sub = (res.pop()-res.pop())
#         #             ans =sub
#         #             print("sub",ans)

#         #         elif i == '*':
#         #             mul = res.pop()*res.pop()
#         #             ans =mul
#         #             print(ans)

#         #         else:
#         #             div= int(res.pop()/res.pop())
#         #             print(div)
#         #             ans = int(ans/div)
#         #     else:
#         #         res.append(int(i))
#         # return ans