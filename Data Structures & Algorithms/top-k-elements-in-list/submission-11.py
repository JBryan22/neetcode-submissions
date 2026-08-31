class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freqBuckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] += 1
        for num, cnt in counts.items():
            freqBuckets[cnt].append(num)
        res = []
        for i in range(len(freqBuckets) - 1, 0, -1):
            for num in freqBuckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                