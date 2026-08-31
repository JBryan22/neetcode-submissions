class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,8,24]
        #[48,48,24,6]

        prefixSums = []
        postfixSums = [0] * len(nums)
        prod = 1

        for num in nums:
            prod *= num
            prefixSums.append(prod)

        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            postfixSums[i] = prod

        res = []
        for i in range(len(nums)):
            pre = 1
            if i != 0:
                pre = prefixSums[i - 1]
            post = 1
            if i <= len(nums) - 2:
                post = postfixSums[i + 1]
            res.append(pre * post)
        return res
