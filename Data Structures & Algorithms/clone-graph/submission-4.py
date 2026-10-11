"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        print(neigh for neigh in node.neighbors)
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        queue = deque([node])
        while queue:
            vertex  = queue.popleft()
            for neigh in vertex.neighbors:
                if neigh not in oldToNew:
                    oldToNew[neigh] = Node(neigh.val)
                    queue.append(neigh)
                oldToNew[vertex].neighbors.append(oldToNew[neigh])
        return oldToNew[node]