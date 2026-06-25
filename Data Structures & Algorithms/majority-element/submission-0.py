class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        majority = (nums[0], 1)
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if (majority[1] < counts[num]):
                majority = (num, counts[num])
        
        return majority[0]