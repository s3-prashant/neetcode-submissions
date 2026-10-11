class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        #Create  a adj list
        adj = defaultdict(list)

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        res = 0
        visit = set()
        minHeap = [[0,0]] #[cost,point]

        while len(visit) < N:

            cost,node = heapq.heappop(minHeap)
            if node in visit:
                continue
            
            res += cost
            visit.add(node)
            for neiCost,neiNode in adj[node]:
                if neiNode not in visit:
                    heapq.heappush(minHeap,[neiCost,neiNode])

        return res
            
