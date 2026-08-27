class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum (nums: List[int], target: int):
            l, r = 0, len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r]
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    return [nums[l], nums[r]]
            return []
        resArr = []
        for i in range(len(nums)):
            res = twoSum(nums[i:], 0 - nums[i])
            if res:
                resArr.append([nums[i], res[0], res[1]])
        return resArr
