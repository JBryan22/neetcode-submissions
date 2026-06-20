class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_chars = {}

        for c in magazine:
            mag_chars[mag_chars.get(c, 0)] += 1

        for c in ransomNote:
            count = mag_chars.get(c, 0)
            if count == 0:
                return False
            mag_chars[mag_chars.get(c, 0)] -= 1
        return True