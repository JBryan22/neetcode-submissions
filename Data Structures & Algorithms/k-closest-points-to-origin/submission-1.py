class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max = []

        for p in points:
            distance = -(math.sqrt(p[0]**2 + p[1]**2))
            if len(max) < k:
                heapq.heappush(max, (distance, p))
            else:
                if distance > max[0][0]:
                    heapq.heappush(max, (distance, p))
                    heapq.heappop(max)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(max)[1])
        return res