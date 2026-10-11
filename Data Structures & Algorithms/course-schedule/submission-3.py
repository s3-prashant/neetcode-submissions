class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            adj[u].append(v)
        visit =set()
        def dfs(node):
            if node in visit:
                return False
            if adj[node] == []:
                return True
            visit.add(node)
            for nei_node in adj[node]:
                
                if not dfs(nei_node):
                    return False
            visit.remove(node)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
            # if  dfs(c):v#will not work
            #     return True

        return True