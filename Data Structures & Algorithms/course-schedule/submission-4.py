class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # d = {i: [] for i in range(numCourses)}
        d = defaultdict(list)

        for course,preq in prerequisites :
            d[course].append(preq)
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False #cycle detected
            if d[course] == []:
                return True
            
            visit.add(course)
            for preq in d[course]:
                if not dfs(preq):
                    return False
            visit.remove(course)
            d[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
