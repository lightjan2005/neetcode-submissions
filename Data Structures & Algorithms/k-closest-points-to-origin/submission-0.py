import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ans = []
        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(ans,[distance,point])

        res = []
        for i in range(k):
            res.append(heapq.heappop(ans)[1])
        
        return res