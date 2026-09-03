class MedianFinder:

    def __init__(self):
        self.lowerMaxH = []
        self.higherMinH = []

    def addNum(self, num: int) -> None:
        if not self.lowerMaxH and not self.higherMinH:
            heapq.heappush(self.lowerMaxH, num * -1)
        elif num > self.lowerMaxH[0] * -1:
            heapq.heappush(self.higherMinH, num)
        else:
            heapq.heappush(self.lowerMaxH, -1 * num)

        if len(self.lowerMaxH) > len(self.higherMinH) + 1:
            popped = heapq.heappop(self.lowerMaxH) * -1
            heapq.heappush(self.higherMinH, popped)
        if len(self.higherMinH) > len(self.lowerMaxH) + 1:
            popped = heapq.heappop(self.higherMinH)
            heapq.heappush(self.lowerMaxH, popped * -1)

    def findMedian(self) -> float:
        if len(self.lowerMaxH) > len(self.higherMinH):
            return self.lowerMaxH[0] * -1
        elif len(self.higherMinH) > len(self.lowerMaxH):
            return self.higherMinH[0]
        else:
            return (self.lowerMaxH[0] * -1 + self.higherMinH[0]) / 2.0
        