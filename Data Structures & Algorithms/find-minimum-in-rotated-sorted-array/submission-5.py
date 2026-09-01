class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = ((hi - lo) // 2) + lo

            if nums[mid] < nums[lo]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]