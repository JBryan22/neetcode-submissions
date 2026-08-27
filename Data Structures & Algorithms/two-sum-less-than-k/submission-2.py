class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return -1

        numsSorted = sorted(nums)

        l, r = 0, len(nums) - 1
        maxNum = -1

        while l < r:
            s = numsSorted[l] + numsSorted[r]

            if s >= k:
                r -= 1
            else:
                maxNum = max(maxNum, s)
                l += 1
        return maxNum

