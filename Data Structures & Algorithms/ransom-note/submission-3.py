class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_chars = {}

        for c in magazine:
            mag_chars[c] = mag_chars.get(c, 0) + 1
            

        for c in ransomNote:
            mag_chars[c] = mag_chars.get(c, 0) - 1
            if mag_chars[c] <= 0:
                return False
        return True