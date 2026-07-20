class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = []
        nums.sort()

        def sumPaths(i: int, currSum: int, currSubset: List[int]):
            if currSum == target:
                subsets.append(currSubset.copy())
                return

            for j in range(i, len(nums)):
                if currSum + nums[j] > target:
                    return
                
                currSubset.append(nums[j])
                sumPaths(j, currSum + nums[j], currSubset)
                currSubset.pop()

        sumPaths(0, 0, [])
        return subsets