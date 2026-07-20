class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = []

        def sumSubsets(i: int, subsets: List[List[int]], currSubset: List[int], currSum: int, target: int):
            if i >= len(nums) or currSum > target:
                return
            
            #choose to add current value
            currSubset.append(nums[i])
            currSum += nums[i]
            if currSum == target:
                subsets.append(currSubset.copy())
                currSubset.pop()
                currSum -= nums[i]
                return
            sumSubsets(i, subsets, currSubset, currSum, target)
            currSubset.pop()
            currSum -= nums[i]

            sumSubsets(i + 1, subsets, currSubset, currSum, target)

        sumSubsets(0, subsets, [], 0, target)
        return subsets