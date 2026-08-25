class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        if len(strs) < 1:
            return longest

        ind = 0
        while True:
            curr = ""
            if ind < len(strs[0]):
                curr = strs[0][ind]
            for word in strs:
                if ind >= len(word) or word[ind] != curr:
                    return longest
            ind += 1
            longest += curr