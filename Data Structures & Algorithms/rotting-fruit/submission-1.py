class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        q = deque()
        # q.append([0,0])
        fresh = 0
        time = 0
        # def rotten(r,c):
        #     if r< 0 or c <0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] ==1:
        #         return
        #     return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [[0,1],[-1,0],[1,0],[0,-1]]
        while  fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    row ,col = r+dr, c+dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

