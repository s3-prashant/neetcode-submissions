class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        #approach to start from treasure and check how many are nearest 
        # INF = 2147483647
        visit = set()
        q = deque()
        def addroom(r,c):
            if (r < 0 or c < 0 or r >=rows or c >=cols or grid[r][c] == -1 or 
            (r,c) in visit):
                return
            
            visit.add((r,c))
            q.append([r,c])


        for r in range(rows):
            for c in range(cols):
                #checking from trasure
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])
        
        # modifying the grid in-place
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
            dist += 1


        


            




