class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        ind = 0
        while ind <= r:
            curr = nums[ind]
            if curr == 0:
                nums[l], nums[ind] = nums[ind], nums[l]
                l += 1
            elif curr == 2:
                nums[r], nums[ind] = nums[ind], nums[r]
                r -= 1
            ind += 1