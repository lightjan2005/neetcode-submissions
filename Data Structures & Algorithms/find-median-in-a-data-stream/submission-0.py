import heapq
class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # maxHeap
        self.rightHeap = [] # minHeap
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        heapq.heappush(self.leftHeap,-num)
        heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
        if len(self.rightHeap) > len(self.leftHeap):
            heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))

    def findMedian(self) -> float:
        if self.length % 2 == 1:
            return -self.leftHeap[0]
        else:
            return (-self.leftHeap[0] + self.rightHeap[0])/2
        