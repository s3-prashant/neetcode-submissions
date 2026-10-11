class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # subsets=defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] +=1
        #     subsets[tuple(count)].append(s)
        # print(subsets)
        # return subsets.values()

        res = {}

        for s in strs:
            sorted_s = sorted(s)
            print(sorted_s)
            key = tuple(sorted_s)
            if key not in res:

                res[key] = [s]
            else:
                res[key].append(s)
        print(res)
        return res.values()