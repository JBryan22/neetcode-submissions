class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # track curr char
        # move right pointer right
            # - if char is diff subtract currDiff
                # - if currDiff < 0
                    # reset currDiff to k
                    # move l to r - k - 1 
            # and 1 add to longest

        l, r = 0, 0
        longest = 0
        windowCount = defaultdict(int)
        mostFreq = 0

        while r < len(s):
            windowCount[s[r]] += 1
            mostFreq = max(windowCount[s[r]], mostFreq)
            if ((r - l + 1) - mostFreq <= k):
                longest = max(longest, r - l + 1)
            else:
                windowCount[s[l]] -= 1
                l += 1
                mostFreq = max(windowCount[s[l]], mostFreq)
            r += 1
        return longest