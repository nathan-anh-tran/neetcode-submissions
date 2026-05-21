class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        #create adj list containing (dist, point)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    p1, p2 = points[i], points[j]
                    adj[i].append((abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), j))
        
        visited = set()
        heap = [(0, 0)]
        total_cost = 0
        while heap:
            cost, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost
            for w, v in adj[u]:
                if v not in visited:
                    heapq.heappush(heap, (w, v))
        return total_cost