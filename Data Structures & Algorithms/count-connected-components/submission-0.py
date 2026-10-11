class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj=defaultdict(list)
        visit = [False] * n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        connected_comp =0
        def dfs(node):
            

            for nei_node in adj[node]:
                if not visit[nei_node]:
                    visit[nei_node] = True
                    dfs(nei_node)
            

        
        
        print(adj)
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                connected_comp+=1
            
        return connected_comp