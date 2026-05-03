import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) < 2:
            return 0
        total = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            price = stick1 + stick2
            total += price
            heapq.heappush(sticks, price)

        return total