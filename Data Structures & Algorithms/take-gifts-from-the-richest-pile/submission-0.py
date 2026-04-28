import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for i in range(k):
            largest = -heapq.heappop(heap)
            remaining = math.floor(math.sqrt(largest))
            heapq.heappush(heap, -remaining)
        return -sum(heap)