class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_subsets, curr_subset = [], []
        nums.sort()

        def helper(idx: int, curr_subset: List[int], all_subsets: List[List[int]]):
            if idx >= len(nums):
                all_subsets.append(curr_subset.copy())
                return

            #path including
            curr_subset.append(nums[idx])
            helper(idx + 1, curr_subset, all_subsets)
            curr_subset.pop()

            #path not including, must skip all duplicates
            while (idx + 1 < len(nums) and nums[idx] == nums[idx + 1]):
                idx += 1

            helper(idx + 1, curr_subset, all_subsets)

        helper(0, curr_subset, all_subsets)
        return all_subsets