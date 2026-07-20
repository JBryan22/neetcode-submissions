class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets, currSet = [], []
        
        def helper(idx: int, currSet: List[int], all_subsets: List[List[int]]):
                if idx >= len(nums):
                    all_subsets.append(currSet.copy())
                    return
                
                #path including the ith num
                currSet.append(nums[idx])
                helper(idx + 1, currSet, all_subsets)
                currSet.pop()

                #path not including the ith num
                helper(idx + 1, currSet, all_subsets)

        helper(0, currSet, all_subsets)
        return all_subsets