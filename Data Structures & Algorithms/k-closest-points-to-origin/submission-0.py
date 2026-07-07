class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x[0]**2 + x[1]**2, x) for x in points]

        heapq.heapify(distances)
        res = []
        for i in range(0, k):
            res.append(heapq.heappop(distances)[1])
        return res