class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s < 2:
            return len(s)
        longest = 0
        seen = set(s[0])
        l, r = 0, 1

        while r < len(s):
            if s[r] in seen:
                longest = max(longest, r - l)
                l = r
            r += 1
        longest = max(longest, r -l)
        return longest