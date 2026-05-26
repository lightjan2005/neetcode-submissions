class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.curTotal = 0
        self.l = 0
        self.r = 0
        self.size = size

    def next(self, val: int) -> float:
        self.r += 1
        self.arr.append(val)
        self.curTotal += val
        if self.r - self.l < self.size:
            return self.curTotal/(self.r) 
        elif self.r - self.l == self.size:
            return self.curTotal/self.size
        else:
            self.curTotal -= self.arr[self.l]
            self.l += 1
            return self.curTotal/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
