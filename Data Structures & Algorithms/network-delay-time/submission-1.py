class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for u,v,time in times:
            adj[u].append([v,time])
        
        shortest = {}
        minHeap = [[0,k]]

        while minHeap:

            t1,n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = t1
            for n2,t2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap,[t1+t2,n2])
        for i in range(1,n+1):
            if i not in shortest:
                return -1
        # print(shortest)
        return max(shortest.values())