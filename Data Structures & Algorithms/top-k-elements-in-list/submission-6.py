class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedNums = sorted(nums, reverse=True)
        res = []
        i = 0
        while i < len(sortedNums):
            res.append(sortedNums[i])
            if len(res) >= k:
                return res
            while i + 1 < len(sortedNums) and sortedNums[i + 1] == sortedNums[i]:
                i += 1
            i += 1
        return res

