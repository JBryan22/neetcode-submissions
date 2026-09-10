class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0

        res = len(nums) + 1
        currTotal = 0

        while r < len(nums):
            currTotal += nums[r]
            while currTotal >= target:
                res = min(res, (r - l) + 1)
                currTotal -= nums[l]
                l += 1
            r += 1

        if res == len(nums) + 1:
            return 0
        return res