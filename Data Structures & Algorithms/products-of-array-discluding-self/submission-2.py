class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for num in nums:
            prod *= num
        
        res = []
        for num in nums:
            res.append(int(prod / num))
        return res