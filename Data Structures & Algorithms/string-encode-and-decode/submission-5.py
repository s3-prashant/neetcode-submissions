class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        if not strs:
            return string
      
        for s in range(len(strs)):
            string += str(len(strs[s])) + "#"
            string += strs[s]
        # string += strs[-1]
        return string
        
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i +length
            res.append(s[i:j])
            i = j
        return res