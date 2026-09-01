class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()

        l = 0

        for r in range(len(nums)):
            while r in seen:
                seen.remove(nums[l])
                l += 1
            longest = max(longest, (r - l) + 1)
        return longest