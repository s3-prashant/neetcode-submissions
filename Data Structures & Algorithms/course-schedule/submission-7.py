class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #build. a graph
        preMap = {i: [] for i in range(numCourses)}
        for crs,preq in prerequisites:
            preMap[crs].append(preq)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for nei in preMap[crs]:
                if not  dfs(nei): 
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True