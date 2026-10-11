class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        g= defaultdict(list)
        for u,v in prerequisites:
            g[u].append(v)
        visit =set()
        cycle=set()
        res=[]
        def dfs(node):
            if node in visit:
                return False
            if node in cycle:
                return True
            
            visit.add(node)
            for  nei in g[node]:
                if not dfs(nei):
                    return False
            res.append(node)
            cycle.add(node)
            visit.remove(node)
            return True
        for c in range(numCourses):
            if dfs(c) ==  False:
                return []
        return res
