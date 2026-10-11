class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >(n-1):
            return False
        if not n :
            return True
        adj = {i:[] for i in range(n)}
        print(adj)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        visit =set()
        def dfs(node,prev):

            if node in visit:
                return False
            visit.add(node)
            for nei_node in adj[node]:
                if nei_node == prev:
                    continue
                if not dfs(nei_node,node):
                    return False
                    
            return True
        return dfs(0,-1) and n==len(visit)