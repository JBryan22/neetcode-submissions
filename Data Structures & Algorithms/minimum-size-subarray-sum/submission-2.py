class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        minLen = len(nums) + 1
        currSum = 0
        while r < len(nums):
            currSum += nums[r]
            while currSum >= target and l <= r:
                minLen = min(minLen, (r - l) + 1)
                currSum -= nums[l]
                l += 1
            r += 1
        if minLen < len(nums):
            return minLen
        else:
            return 0