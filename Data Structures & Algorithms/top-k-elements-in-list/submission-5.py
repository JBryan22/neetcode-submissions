class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedNums = sorted(nums, reverse=True)
        res = []
        i = 0
        while i < len(nums):
            res.append(nums[i])
            if len(res) >= k:
                return res
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return res

