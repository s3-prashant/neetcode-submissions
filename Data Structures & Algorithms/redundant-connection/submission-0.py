class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        D = defaultdict(list)
        
        def dfs(node,parent):
            if visit[node]:
                return True
            visit[node] = True
            for nei_node in D[node]:
                if nei_node == parent:
                    continue
                if dfs(nei_node,node):
                    return True
            return False
        
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
            # print(D)
            visit = [False] *(len(edges)+1)
            if dfs(u,-1):
                return [u,v]
        return []



        

        # q = deque()
        # q.append(edges[0][0])
        # seen = set()
        # while q:
        #     node = q.popleft()
        #     for nei_node in D[node]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             q.append(nei_node)

        #     res = D[node]
       
        # return res
