class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            ind = abs(num) - 1
