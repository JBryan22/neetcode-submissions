class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            prod *= num
        
        if zeroCount > 1:
            return [[0] * len(nums)]
        res = []
        for num in nums:
            if zeroCount == 1 and num != 0:
                res.append(0)
            elif num == 0:
                res.append(prod)
            else:
                res.append(int(prod / num))
        return res