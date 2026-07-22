class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        candidates.sort()

        def comboSums(i: int, curr_subset: List[int], curr_total: int):
            if curr_total == target:
                subsets.append(curr_subset.copy())
            
            if curr_total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] + curr_total > target:
                    return
                
                curr_subset.append(candidates[j])
                comboSums(j + 1, curr_subset, curr_total + candidates[j])
                curr_subset.pop()
        
        comboSums(0, [], 0)
        return subsets