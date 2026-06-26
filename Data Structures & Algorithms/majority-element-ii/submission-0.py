class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        majority = (len(nums) // 3) + 1
        res = []

        for num in nums:
            counter[num] += 1
            if counter[num] == majority:
                res.append(num)
        return res