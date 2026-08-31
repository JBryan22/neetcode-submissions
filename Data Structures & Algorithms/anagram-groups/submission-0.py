class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [tuple(sorted(s)).append(s)]
        return res
