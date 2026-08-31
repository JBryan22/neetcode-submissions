class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            counts = Counter(s)

            res[frozenset(counts)].append(s)
        
        return list(res.values())