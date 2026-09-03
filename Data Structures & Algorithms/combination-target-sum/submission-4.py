class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def findCombos(currSubset:List[int], i: int, currSum: int):
            if currSum == target:
                res.append(currSubset.copy())
            
            for j in range(i, len(nums)):
                if currSum + nums[j] > target:
                    return
                
                currSubset.append(nums[j])
                findCombos(currSubset, j, currSum + nums[j])
                currSubset.pop()

        findCombos([], 0, 0)
        return res