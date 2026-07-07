class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = []

        for n in nums:
            if len(minH) < k:
                heapq.heappush(minH, n)
            else:
                if n > minH[0]:
                    heapq.heappush(minH, n)
                    heapq.heappop(minH)
        
        return heapq.heappop(minH)