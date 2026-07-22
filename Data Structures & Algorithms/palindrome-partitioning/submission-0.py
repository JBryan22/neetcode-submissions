class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str, l: int, r: int) -> bool:
            if len(s) == 0:
                return False
            if len(s) < 2:
                return True
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        subsets = []
        curr_str = []

        def palinPart(depth: int):
            if depth == len(s):
                subsets.append(curr_str.copy())
                return
            for j in range(depth, len(s)):
                if isPalindrome(s, depth, j):
                    curr_str.append(s[depth:j+1])
                    palinPart(j+1)
                    curr_str.pop()
            

        palinPart(0)
        return subsets