class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adjs = collections.defaultdict(list)
        shortest = {}
        
        for i in range(len(edges)):
            u,v,w = edges[i]
            adjs[u].append((v,w))
        
        minHeap = [(0, src)]
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in shortest:
                continue

            shortest[node] = weight            
            for node2, weight2 in adjs[node]:
                if node2 not in shortest:
                    heapq.heappush(minHeap, (weight + weight2, node2))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest