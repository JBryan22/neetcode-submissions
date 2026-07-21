class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        candidates.sort()

        def pathSums(i: int, currSubset: List[int], currTotal: int):
            if currTotal == target:
                subsets.append(currSubset.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if currTotal + candidates[j] > target:
                    return
                
                currSubset.append(candidates[j])
                pathSums(j + 1, currSubset, currTotal + candidates[j])
                currSubset.pop()
            
        pathSums(0, [], 0)
        return subsets