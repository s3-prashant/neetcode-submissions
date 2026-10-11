class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        visit = set()
        queue = deque()
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r,c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and queue:

            for _ in range(len(queue)):
                row,col = queue.popleft()
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) 
                    and grid[r][c] == 1):
                        grid[r][c] = 2
                        queue.append([r,c])
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1