import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)

        for c in s1:
            mp[c] += 1

        currMap = copy.deepcopy(mp)
        l, r = 0, 0

        while r < len(s2):
            char = s2[r]
            if char in currMap:
                currMap[char] -= 1
                if currMap[char] == 0:
                    del currMap[char]
                    if not currMap:
                        return True
            r += 1
            if r - l == len(s1):
                if s2[l] in mp:
                    currMap[s2[l]] += 1
                l += 1
        return False
                
                