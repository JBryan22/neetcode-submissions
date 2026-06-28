class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        l, r = 0, 0
        inWindow = set()

        while r < len(s):
            curr += 1
            while (s[r] in inWindow):
                inWindow.discard(s[l])
                l += 1
                curr -= 1
            longest = max(curr, longest)
            inWindow.add(s[r])
            r += 1

        return longest