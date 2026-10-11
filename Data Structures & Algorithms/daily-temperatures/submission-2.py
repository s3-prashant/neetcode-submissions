class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] # pair: [temp,index]
        for i,t in enumerate(temperatures):

            while stack and t > stack[-1][0]: 
                #check if stack exists and current temp > top of stack element
                #popping index, temp from stack

                stackTemp, stackIndex = stack.pop() # [30,0]
                #will update the result with days ()
                res[stackIndex] = (i-stackIndex)
            stack.append([t,i]) # adding a pair
        return res
