class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = [False] * n
        connected_components = 0

        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)

        def dfs(node):

            for nei in adj[node]:
                if  not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                connected_components += 1
        return connected_components