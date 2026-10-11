


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
                
            return memo[(i, j)]
        
        return dfs(0, 0)




# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         m,n=len(text1),len(text2)
#         # def longest(i,j):
#             if i==m or j==n:
#                 return 0
#             elif text1[i]==text2[j]:
#                 return 1+longest(i+1,j+1)
#             else:
#                 return max(longest(i+1,j),longest(i,j+1))

#         return longest(0,0)