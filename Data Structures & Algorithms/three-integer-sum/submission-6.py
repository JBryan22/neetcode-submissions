class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        numSorted = sorted(nums)

        start = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                break
            start = i
        
        for i in range(len(nums)):
            l, r = start + 1, len(nums) - 1
            while l < r:
                threeS = nums[start] + nums[l] + nums[r]

                if threeS > 0:
                    r -= 1
                elif threeS < 0:
                    l += 1
                else:
                    res.append([nums[start], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    r += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r += 1
        return res
