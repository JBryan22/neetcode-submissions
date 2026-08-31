class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        minH = []
        for num, cnt in counts.items():
            heapq.heappush(minH, (cnt, num))
            if len(minH) > k:
                heapq.heappop(minH)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(minH)[1])
        return res