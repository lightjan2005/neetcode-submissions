import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        heap = [(num, i)for i, num in enumerate(nums)]
        heapq.heapify(heap)

        for i in range(k):
            num, i = heapq.heappop(heap)
            num *= multiplier
            heapq.heappush(heap,(num,i))

        ans = [0 for i in range(len(nums))]
        for i in range(len(heap)):
            num, index = heapq.heappop(heap)
            ans[index] = num

        return ans