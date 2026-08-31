class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = defaultdict(int)

        for i in range(len(s)):
            counts[s[i]] += 1
        
        for i in range(len(t)):
            counts[s[i]] -= 1
        
        for c in counts.values():
            if c != 0:
                return False
        
        return True
