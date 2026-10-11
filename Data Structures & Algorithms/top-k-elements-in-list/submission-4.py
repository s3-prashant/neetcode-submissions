# class Solution:
#     def topKFrequent(self, nums: List[int], ki: int) -> List[int]:
#         # d=defaultdict(list)
#         d= {}
#         c=[]
#         for i in nums:
#             d[i] = 1 + d.get(i,0)
#         for k,v in d.items():
#             if v >= ki:
#                 c.append(k)
#         return c

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
