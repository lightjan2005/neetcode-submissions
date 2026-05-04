import heapq
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        distanceHeap = []
        ans = [0 for i in range(len(workers))]
        for workerIndex, worker in enumerate(workers):
            workerX, workerY = worker
            for bikeIndex, bike in enumerate(bikes):
                bikeX, bikeY = bike
                distance = abs(workerX - bikeX) + abs(workerY - bikeY)
                heapq.heappush(distanceHeap, [distance, workerIndex, bikeIndex])
        seenWorkers = set()
        seenBikes = set()

        while len(seenWorkers) < len(workers):
            d, w, b = heapq.heappop(distanceHeap)
            if w not in seenWorkers and b not in seenBikes:
                seenWorkers.add(w)
                seenBikes.add(b)
                ans[w] = b

        return ans