class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 3:
            return True
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalnum():
                left += 1
                if left > right:
                    return False
            while not s[right].isalnum():
                right -= 1
                if right < left:
                    return False
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True