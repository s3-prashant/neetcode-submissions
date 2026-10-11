class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for string in strs:
            sorted_str = sorted(string)
            key  = tuple(sorted_str)
            if key in res:
                res[key].append(string)
            else:
                res[key] = [string]
        # output = []
        # for values in res.values():
        #     output.append(values)
        # print(res)
        return list(res.values())