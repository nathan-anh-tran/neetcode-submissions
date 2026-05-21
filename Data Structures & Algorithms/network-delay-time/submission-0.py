class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #do dijkstra's from node k until all nodes are hit
        #add up total weights
        #if not all nodes are hit return -1

        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        dist = [float("inf")] * (n + 1)
        dist[0] = 0
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            cost, curr_node = heapq.heappop(heap)
            if cost > dist[curr_node]:
                continue
            for neighbor, weight in adj[curr_node]:
                if dist[curr_node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[curr_node] + weight
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        if float("inf") in dist:
            return -1
        else:
            return max(dist)