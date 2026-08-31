class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,8,24]
        #[48,48,24,6]

        prefixSums = []
        postfixSums = []
        prod = 1

        for num in nums:
            prod *= num
            prefixSums.append(prod)

        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            postfixSums.append(prod)

        res = []
        for i in range(len(nums)):
            pre = 1
            if i != 0:
                pre = nums[i - 1]
            post = 1
            if i <= len(nums) - 2:
                post = nums[i + 1]
            res.append(pre * post)
        return res
