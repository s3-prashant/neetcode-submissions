class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows,cols = len(grid),len(grid[0])
        #approach to start from treasure and check how many are nearest 
        # INF = 2147483647
        visit = set()
        queue = deque()

        def addroom(r,c):
            if (r < 0 or r >= rows or c <0 or c >= cols or grid[r][c] == -1 or 
            (r,c) in visit ):
                return
            visit.add((r,c))
            queue.append([r,c])


        for r in range(rows):
            for c in range(cols):
                #checking from trasure
                if grid[r][c] == 0:
                    visit.add((r,c))
                    queue.append([r,c])
        
        # modifying the grid in-place
        distance = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = distance
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
            distance += 1
        