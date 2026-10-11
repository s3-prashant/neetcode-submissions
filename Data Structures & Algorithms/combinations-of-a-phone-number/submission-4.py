class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {"2" : ['a','b','c'] , "3" : ['d','e','f'] ,"4":['g','h','i'] ,
        "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['q','p','r','s'],
            "8":['t','u','v'],
            "9": ['w','x','y','z']}
        res=[""]
        if digits =="":
            return []
        if len(digits) ==1:
            return d[digits[0]]
        
        for digit in digits:
            temp = []
            for curstr in res:
                for c in d[digit]:
                    temp.append(curstr+c)
            res = temp
        return res
        # for k in range(len(digits)):
        #     for i in range(len(d[digits[k]])):
        #         # s=d[digits[0]][i]
        #         for j in range(len(d[digits[k+1]])):
        #             s=d[digits[0]][i]
        #             s+= d[digits[1]][j]
        #             res.append(s)
        #             s=""
        #             print(s)
        # return res
