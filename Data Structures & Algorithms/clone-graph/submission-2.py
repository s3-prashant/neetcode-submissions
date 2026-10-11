"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        D=defaultdict(list)

        # for u,v in D:
        #     D[u].append(node.val)

        def dfs(node):
            if node in D:
                return D[node]
            copy=Node(node.val)
            D[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy



        return dfs(node) if node else None