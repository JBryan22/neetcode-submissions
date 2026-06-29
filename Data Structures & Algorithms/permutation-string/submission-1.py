class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)

        for c in s1:
            mp[c] += 1

        needToMatch = len(mp)
        matchCount = 0
        l, r = 0, 0

        while r < len(s2):
            char = s2[r]
            if char in mp:
                if mp[char] == 0:
                    matchCount -= 1
                mp[char] -= 1
                if mp[char] == 0:
                    matchCount += 1
                    if matchCount == needToMatch:
                        return True
            r += 1
            if r - l == len(s1):
                if s2[l] in mp:
                    if mp[s2[l]] == 0:
                        matchCount -= 1
                    mp[s2[l]] += 1
                    if mp[s2[l]] == 0:
                        matchCount += 1
                        if matchCount == needToMatch:
                            return True
                l += 1
        return False
                