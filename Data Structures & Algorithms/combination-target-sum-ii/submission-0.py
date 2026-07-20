class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []

        def sumPaths(i: int, currSubset: List[int], currTotal: int):
            if currTotal == target:
                subsets.append(currSubset.copy())
                return
            if currTotal > target or i >= len(candidates):
                return

            currSubset.append(candidates[i])
            sumPaths(i + 1, currSubset, currTotal + candidates[i])
            currSubset.pop()

            while (i + 1 < len(candidates) and candidates[i] == candidates[i + 1]):
                i+=1
            sumPaths(i + 1, currSubset, currTotal)
        
        sumPaths(0, [], 0)
        return subsets